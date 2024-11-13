def add_students(students):
    student = {}
    
    student["name"] = input("Name: ")
    student["section"] = input("Section: ")
    
    student["notes"] = {}
    student["notes"]["spanish"] = validate_grade("Enter Spanish note: ")
    student["notes"]["english"] = validate_grade("Enter English note: ")
    student["notes"]["socials"] = validate_grade("Enter Socials note: ")
    student["notes"]["science"] = validate_grade("Enter Science note: ")

    students.append(student)
    print(f"Student {student['name']} has been added.")

    return student


def validate_grade(prompt):
    while True:
        try:
            note = float(input(prompt))
            if 0 <= note <= 100:
                return note
            else:
                print("Note must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def show_all_students(students):
    if students:
        for student in students:
            print(f"{student['name']} ({student['section']}): {student['notes']}")
    else:
        print("No students available")


def show_top_3_students(students):
    students_sorted = sorted(students, key=lambda x: sum(x['notes'].values()) / 4, reverse=True)
    top_3 = students_sorted[:3]
    print("Top 3 students:")
    for student in top_3:
        avg_score = sum(student['notes'].values())/4
        print(f"{student['name']} - Average: {avg_score:.2f}")


def show_average_score(students):
    if students:
        total_score = sum(sum(student['notes'].values()) for student in students)
        total_students = len(students)
        avg_score = total_score / (total_students * 4)
        print(f"Average score of all students: {avg_score:.2f}")
    else:
        print("No students available")