import csv
import os


def export_to_csv(students):
    if not students:
        print("No data to export")
        return
    

    with open('students_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Section', 'Spanish', 'English', 'Socials', 'Science'])


        for student in students:
            writer.writerow([student['name'], student['section'], student['notes']['spanish'],student['notes']['english'], student['notes']['socials'], student['notes']['science']])

    print("Data exported successfully to 'students_data.csv'.")


def import_from_csv():
    if not os.path.exists('students_data.csv'):
        print("No previous data found. Please export data first.")
        return []
    

    students = []
    try:
        with open('students_data.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for row in reader:
                student = {
                    "name": row[0],
                    "section": row[1],
                    "notes": {
                        "spanish": float(row[2]),
                        "english": float(row[3]),
                        "socials": float(row[4]),
                        "science": float(row[5]),
                    },
                }
                students.append(student)
        print(f"Data import from {'students_data.csv'}")
    except FileNotFoundError:
        print("File does not exist.")
    return students

