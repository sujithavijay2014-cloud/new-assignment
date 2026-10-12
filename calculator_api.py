from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send JSON data"}), 400

    try:
        a = float(data["a"])
        b = float(data["b"])
        operation = data["operation"]
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Enter valid a, b and operation"}), 400

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Unknown operation"}), 400

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)