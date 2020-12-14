from model.crm import crm
from model import util
from view import terminal as view


def list_customers():

    view.print_message("List of Customers:\n")
    view.print_table(crm.get_crm_table_from_file())
    view.get_input("Press ENTER to return to MAIN MENU")


def add_customer():

    list_of_customers = crm.get_crm_table_from_file()
    view.print_table(list_of_customers)
    customer_data = crm.HEADERS[1:]
    continue_add = "y"

    while continue_add.lower() in ["y", "yes"]:
        new_customer = [util.generate_id()] + view.get_inputs(customer_data)
        list_of_customers.append(new_customer)
        view.print_message("Succesfully added new customer.")
        continue_add = view.get_input("Do you want to add another customer? (y/n)")

    crm.write_crm_table_to_file(list_of_customers)
    view.get_input("Press ENTER to return to MAIN MENU")


def update_customer():

    list_customers = crm.get_crm_table_from_file()
    view.print_table(list_customers)
    customer_data = crm.HEADERS[1:]
    ID_index = crm.HEADERS.index("id")
    found_ID = False

    while not found_ID:
        customer_id = view.get_input("Enter the customer ID number: ")
        for customer in list_customers:
            if customer[ID_index] == customer_id:
                customer[1:] = view.get_inputs(customer_data)
                found_ID = True

        if not found_ID:
            user_input = ""
            while user_input.lower() not in ["n", "no", "y", "yes"]:
                view.print_message("The ID provided matches no customer.")
                user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_ID = True

    crm.write_crm_table_to_file(list_customers)
    view.get_input("Press ENTER to return to MAIN MENU")


def delete_customer():

    list_of_customers = crm.get_crm_table_from_file()
    view.print_table(list_of_customers)
    ID_index = crm.HEADERS.index("id")
    found_ID = False

    while not found_ID:
        customer_id = view.get_input("Enter the customer ID number: ")
        for customer in list_of_customers:
            if customer[ID_index] == customer_id:
                list_of_customers.remove(customer)
                view.print_message(f"Customer with id {customer_id} has been deleted.")
                found_ID = True

        if not found_ID:
            view.print_message("The ID provided matches no customer.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_ID = True

    crm.write_crm_table_to_file(list_of_customers)
    view.get_input("Press ENTER to return to MAIN MENU")


def get_subscribed_emails():
    
    table = crm.get_crm_table_from_file()
    subscribed_emails = []
    subscribed = [1, "1"]
    email_index = crm.HEADERS.index("email")
    subscr_index = crm.HEADERS.index("subscribed")

    [subscribed_emails.append(person[email_index]) for person in table if person[subscr_index] in subscribed]

    view.print_general_results(subscribed_emails, "The subscribed emails")
    view.get_input("Press ENTER to return to MAIN MENU")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
