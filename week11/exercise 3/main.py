import menu 
import actions
import data


def run_program():
    students = []

    while True:
        menu.display_menu()
        user_option = menu.get_user_option()

        if user_option == 1:
            actions.add_students(students)
        elif user_option == 2:
            actions.show_all_students(students)
        elif user_option == 3:
            actions.show_top_3_students(students)
        elif user_option == 4:
            actions.show_average_score(students)
        elif user_option == 5:
            data.export_to_csv(students)
        elif user_option == 6:
            students = data.import_from_csv()
        elif user_option == 7:
            print("Exiting..")
            break
        else:
            print("Invalid option, please try again.")


run_program ()



