from model import util
from model.hr import hr
from view import terminal as view
from datetime import datetime


def list_employees():
    list_of_employees = hr.get_hr_table_from_file()
    view.print_message("List of Emplyees\n")
    view.print_table(list_of_employees)
    view.press_enter()
    
    #view.print_error_message("Not implemented yet.")


def add_employee():
    list_of_employees = hr.get_hr_table_from_file()
    employee_data = hr.HEADERS[1:]
    continue_adding = "y"

    while continue_adding.lower() in ["y", "yes"]:
        new_employee = [util.generate_id()] + view.get_inputs(employee_data)
        list_of_employees.append(new_employee)
        continue_adding = view.get_input("Do you want to add another employee? (y/n): ")
    
    hr.write_hr_table_to_file(list_of_employees)
    view.print_message("A new employee has been added")
    
    #view.print_error_message("Not implemented yet.")
    

def update_employee():
    list_of_employees = hr.get_hr_table_from_file()
    employee_data = hr.HEADERS[1:]
    ID_index = 0
    found_ID = False

    while not found_ID:
        employee_ID = view.get_input("Please, enter the employee's ID number: ")
        for employee in list_of_employees:
            if employee[ID_index] == employee_ID:
                employee[1:] = view.get_inputs(employee_data)
                found_ID = True
                break
        
        if not found_ID:
            user_input = ""
            while user_input.lower() not in ['n', 'no', 'y', 'yes']:
                user_input = view.get_input("The ID provided matches no employee. Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ['n', 'no']:
                found_ID = True

    hr.write_hr_table_to_file(list_of_employees)

    #view.print_error_message("Not implemented yet.")


def delete_employee():
    list_of_employees = hr.get_hr_table_from_file()
    view.print_table(list_of_employees)
    found_iD = False
    ID_index = 0

    while not found_iD:
        employee_id = view.get_input("Please, enter the employee's ID number: ")
        for employee in list_of_employees:
            if employee[ID_index] == employee_id:
                list_of_employees.remove(employee)
                found_iD = True
        if not found_iD:
            view.print_error_message("The ID provided matches no employee.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_iD = True

    hr.write_hr_table_to_file(list_of_employees)
    view.print_message(f"Employee with id {employee_id} has been deleted.")
    view.press_enter()

    # view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():

    list_of_employees = hr.get_hr_table_from_file()
    birth_date_id = 2
    oldest_and_youngest = {"Oldest": list_of_employees[1], "Youngest": list_of_employees[1]}
    

    for employee_index in range(1, len(list_of_employees)):
        employee_date_birth = datetime.strptime(list_of_employees[employee_index][birth_date_id], "%Y-%m-%d")
        oldest_date_birth = datetime.strptime(oldest_and_youngest.get("Oldest")[birth_date_id], "%Y-%m-%d")
        youngest_date_birth = datetime.strptime(oldest_and_youngest.get("Youngest")[birth_date_id], "%Y-%m-%d")

        if employee_date_birth < oldest_date_birth:
            oldest_and_youngest["Oldest"] = list_of_employees[employee_index]
        elif employee_date_birth > youngest_date_birth:
            oldest_and_youngest["Youngest"] = list_of_employees[employee_index]

    view.print_general_results(oldest_and_youngest, "Oldest and youngest employees: ")
    view.press_enter()

    # view.print_error_message("Not implemented yet.")

def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
