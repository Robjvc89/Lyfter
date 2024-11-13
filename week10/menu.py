def display_menu():
    print("\nMenu Options:")
    print("1. Add students")
    print("2. View all students")
    print("3. View top 3 students by average score")
    print("4. View average score of all students")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. Exit")


def get_user_option():
    try:
        option = int(input("Enter your choice: "))
        return option
    except ValueError:
        print("Please enter a valid number")
        return -1