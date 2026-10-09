students = []


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject} mark (0-100): "))

            if 0 <= mark <= 100:
                return mark

            print("0 mudhal 100 varaikkum mark kodunga.")

        except ValueError:
            print("Ennai mattum kodunga. Example: 85")








def add_student():
    name = input("Student peyar: ").strip()

    if not name:
        print("Peyar kaaliyaga irukka koodathu.")
        return

    tamil = get_mark("Tamil")
    english = get_mark("English")
    maths = get_mark("Maths")

    total = tamil + english + maths
    average = total / 3

    if min(tamil, english, maths) < 35:
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "E"

    students.append({
        "name": name,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    })

    print("\n--- Student Result ---")
    print("Name:", name)
    print(f"Total: {total:.1f} / 300")
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
    print("Result:", result)


def show_students():
    if not students:
        print("Innum students add pannala.")
        return

    print("\n--- All Students ---")

    for number, student in enumerate(students, start=1):
        print(
            f"{number}. {student['name']} | "
            f"Total: {student['total']:.1f} | "
            f"Average: {student['average']:.2f} | "
            f"Grade: {student['grade']} | "
            f"Result: {student['result']}"
        )


while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Exit")

    choice = input("Option select pannunga (1/2/3): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Program mudinthathu. Thank you!")
        break
    else:
        print("1, 2, allathu 3 kodunga.")