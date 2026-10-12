import streamlit as st

st.title("My First Calculator")
st.write("Rendu numbers kuduthu calculate pannunga!")

a = st.number_input("First number", value=0.0)
b = st.number_input("Second number", value=0.0)

operation = st.selectbox(
    "Enna calculation?",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    else:
        if b == 0:
            st.error("Zero-va vechu divide panna mudiyathu!")
            st.stop()
        result = a / b

    st.success(f"Answer: {result}")