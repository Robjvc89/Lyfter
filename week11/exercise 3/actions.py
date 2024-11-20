from student import Student

def add_students(students):
    print("\nEnter student information:")
    name = input("Name: ")
    section = input("Section: ")
    
    notes = []
    for subject in ["Spanish", "English", "Social", "Science"]:
        while True:
            try:
                note = float(input(f"Note in {subject}"))
                if 0 <= note <= 100:
                    notes.append(note)
                    break
                else:
                    print("Note must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    student = Student(name, section, *notes)
    students.append(student)
    print(f"Student {name} has been added.")
    return students


def show_all_students(students):
    if students:
        for student in students:
            print(f"{student.name} ({student.section}): {student.notes}")
    else:
        print("No students available")


def show_top_3_students(students):
    students_sorted = sorted(students, key=lambda x: sum(x.notes.values()) / 4, reverse=True)
    top_3 = students_sorted[:3]
    print("Top 3 students:")
    for i in range(min(3, len(students_sorted))):
        student = students_sorted[i]
        print(f"Rank {i+1}: {student.name} ({student.section}) - Average: {student.average:.2f}")


def show_average_score(students):
    if students:
        total_score = sum(sum(student.notes.values()) for student in students)
        total_students = len(students)
        avg_score = total_score / (total_students * 4)
        print(f"Average score of all students: {avg_score:.2f}")
    else:
        print("No students available")