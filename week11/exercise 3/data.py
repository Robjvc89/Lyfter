import csv
import os
from student import Student


def export_to_csv(students):
    if not students:
        print("No data to export")
        return
    
    try:
        fieldnames = ['name', 'section', 'Spanish', 'English', 'Social', 'Science', 'average']

        with open('students_data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                student_dict = student.to_dict()  
    
                writer.writerow({
                    'name': student_dict['name'],
                    'section': student_dict['section'],
                    'Spanish': student_dict['notes']['Spanish'],
                    'English': student_dict['notes']['English'],
                    'Social': student_dict['notes']['Social'],
                    'Science': student_dict['notes']['Science'],
                    'average': student_dict['average']
                })
        print("Data exported successfully to 'students_data.csv'.")
    except Exception as e:
        print(f"Error exporting data: {e}")


def import_from_csv():
    if not os.path.exists('students_data.csv'):
        print("No previous data found. Please export data first.")
        return []
    

    students = []
    try:
        with open('students_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            print("CSV Headers:", reader.fieldnames)

            for row in reader:
                print("Row data:", row)
            
                student_data = {
                "name": row["name"],
                "Spanish": row["Spanish"],
                "English": row["English"],
                "Social": row["Social"],
                "Science": row["Science"]
            }
            
        
        print("Data exported successfully to 'students_data.csv'.")

    except FileNotFoundError:
        print("File does not exist.")
    return students

