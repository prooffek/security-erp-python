from model import util
from model.hr import hr
from view import terminal as view
from datetime import datetime, date, timedelta


def list_employees():

    view.print_message("List of Employees:\n")
    view.print_table(hr.get_hr_table_from_file())
    view.get_input("Press ENTER to return to MAIN MENU")


def add_employee():

    list_of_employees = hr.get_hr_table_from_file()
    employee_data = hr.HEADERS[1:]
    continue_adding = "y"

    while continue_adding.lower() in ["y", "yes"]:
        new_employee = [util.generate_id()] + view.get_inputs(employee_data)
        list_of_employees.append(new_employee)
        view.print_message("Succesfully added new employee.")
        continue_adding = view.get_input("Do you want to add another employee? (y/n): ")

    hr.write_hr_table_to_file(list_of_employees)
    view.get_input("Press ENTER to return to MAIN MENU")


def update_employee():

    list_of_employees = hr.get_hr_table_from_file()
    view.print_table(list_of_employees)
    employee_data = hr.HEADERS[1:]
    ID_index = hr.HEADERS.index("Id")
    found_ID = False

    while not found_ID:
        employee_ID = view.get_input("Enter the employee's ID number: ")
        for employee in list_of_employees:
            if employee[ID_index] == employee_ID:
                employee[1:] = view.get_inputs(employee_data)
                view.print_message(f"Employee with id {employee_id} has been updated.")
                found_ID = True

        if not found_ID:
            user_input = ""
            while user_input.lower() not in ['n', 'no', 'y', 'yes']:
                view.print_message("The ID provided matches no employee.")
                user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ['n', 'no']:
                found_ID = True

    hr.write_hr_table_to_file(list_of_employees)
    view.get_input("Press ENTER to return to MAIN MENU")


def delete_employee():

    list_of_employees = hr.get_hr_table_from_file()
    view.print_table(list_of_employees)
    found_iD = False
    ID_index = 0

    while not found_iD:
        employee_id = view.get_input("Enter the employee's ID number: ")
        for employee in list_of_employees:
            if employee[ID_index] == employee_id:
                list_of_employees.remove(employee)
                view.print_message(f"Employee with id {employee_id} has been deleted.")
                found_iD = True
        if not found_iD:
            view.print_error_message("The ID provided matches no employee.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_iD = True

    hr.write_hr_table_to_file(list_of_employees)
    view.get_input("Press ENTER to return to MAIN MENU")


def get_oldest_and_youngest():

    list_of_employees = hr.get_hr_table_from_file()
    birth_date_index = hr.HEADERS.index("Date of birth")
    name_index = hr.HEADERS.index("Name")
    oldest = list_of_employees[1]
    youngest = list_of_employees[1]
    oldest_and_youngest = {"Oldest": oldest[name_index], "Youngest": youngest[name_index]}

    for employee in list_of_employees[1:]:
        employee_date_birth = datetime.strptime(employee[birth_date_index], "%Y-%m-%d")
        oldest_date_birth = datetime.strptime(oldest[birth_date_index], "%Y-%m-%d")
        youngest_date_birth = datetime.strptime(youngest[birth_date_index], "%Y-%m-%d")

        if employee_date_birth < oldest_date_birth:
            oldest_and_youngest["Oldest"] = employee[name_index]
            oldest = employee
        elif employee_date_birth > youngest_date_birth:
            oldest_and_youngest["Youngest"] = employee[name_index]
            youngest = employee

    view.print_general_results(oldest_and_youngest, "Oldest and youngest employees: ")
    view.get_input("Press ENTER to return to MAIN MENU")


def get_average_age():

    list_of_employees = hr.get_hr_table_from_file()
    separator = "-"
    date_of_birth_index = hr.HEADERS.index("Date of birth")
    current_year, current_month, current_day = str(date.today()).split(separator)

    age = 0
    for employee in list_of_employees[1:]:
        date_of_birth = employee[date_of_birth_index]
        birth_year, birth_month, birth_day = str(date.fromisoformat(date_of_birth)).split(separator)

        if int(birth_month) >= int(current_month) and int(birth_day) > int(current_day):
            age += int(current_year) - int(birth_year) - 1
        else:
            age += int(current_year) - int(birth_year)

    view.print_general_results(age/len(list_of_employees), "Employees' avarage age is")
    view.get_input("Press ENTER to return to MAIN MENU")


def next_birthdays():

    list_of_employees = hr.get_hr_table_from_file()
    birth_date_index = hr.HEADERS.index("Date of birth")
    name_index = hr.HEADERS.index("Name")
    time_delta = 14
    current_date = date.today()
    next_date = current_date + timedelta(time_delta)
    names = []
    table = [hr.HEADERS]

    for employee in list_of_employees[1:]:
        date_birth_employee = datetime.strptime(employee[birth_date_index], "%Y-%m-%d").date()
        if date_birth_employee.strftime('%m-%d') >= current_date.strftime('%m-%d') and date_birth_employee.strftime('%m-%d') <= next_date.strftime('%m-%d'):
            names.append(employee[name_index])
            table.append(employee)
    if len(names) == 0:
        view.print_message("No employee has a birthday in the next two weeks.")
    else:
        view.print_general_results(names, "Employees with birthdays in the next two weeks: \n")
        view.print_table(table)
    view.get_input("Press ENTER to return to MAIN MENU")


def count_employees_with_clearance():

    list_of_employees = hr.get_hr_table_from_file()
    clearance_index = hr.HEADERS.index("Clearance")
    num_of_employees = 0

    clearance = view.get_input("Specify the clearance level: ")

    for employee in list_of_employees[1:]:
        if int(employee[clearance_index]) >= int(clearance):
            num_of_employees += 1

    view.print_general_results(num_of_employees, f"The number of employees with at least clearance level {clearance} is")
    view.get_input("Press ENTER to return to MAIN MENU")


def count_employees_per_department():

    list_of_employees = hr.get_hr_table_from_file()
    department_index = hr.HEADERS.index("Department")
    employees_department_count = {}

    for employee in list_of_employees[1:]:
        if employee[department_index] not in employees_department_count:
            employees_department_count[employee[department_index]] = 1
        else:
            employees_department_count[employee[department_index]] += 1

    view.print_general_results(employees_department_count, "The number of employees per department is:")
    view.get_input("Press ENTER to return to MAIN MENU")


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
