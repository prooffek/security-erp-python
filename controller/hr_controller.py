from model import util
from model.hr import hr
from view import terminal as view
from datetime import date


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
    view.print_error_message("Not implemented yet.")


def get_average_age():
    list_of_employees = hr.get_hr_table_from_file()
    list_without_header = list_of_employees[1:]
    separator = "-"
    date_of_birth_index = hr.HEADERS.index("Date of birth")
    current_year, current_month, current_day = str(date.today()).split(separator)
    
    age = 0
    for employee in list_without_header:
        date_of_birth = employee[date_of_birth_index]
        birth_year, birth_month, birth_day = str(date.fromisoformat(date_of_birth)).split(separator)

        if int(birth_month) >= int(current_month) and int(birth_day) > int(current_day):
            age += int(current_year) - int(birth_year) - 1
        else:
            age += int(current_year) - int(birth_year)

    view.print_general_results(age/len(list_without_header), "Employees' avarage age is")
    view.press_enter()

    #view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    list_of_employees = hr.get_hr_table_from_file()
    clearance_index = hr.HEADERS.index("Clearance")
    num_of_employees = 0

    clearance = view.get_input("Specify the clearance level: ")

    for employee in list_of_employees[1:]:
        if int(employee[clearance_index]) >= int(clearance):
            num_of_employees += 1

    view.print_general_results(num_of_employees, f"The number of employees with at least clearance level {clearance} is")
    view.press_enter()

    #view.print_error_message("Not implemented yet.")


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
