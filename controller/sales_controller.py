from model.sales import sales
from view import terminal as view
from model import util
from datetime import datetime


def list_transactions():
    view.print_table(sales.read_table())
    view.press_enter()

    #view.print_error_message("Not implemented yet.")


def add_transaction():
    list_of_transactions = sales.read_table()
    transactions_data = sales.HEADERS[1:]
    continue_adding = "y"

    while continue_adding.lower() in ["y", "yes"]:
        new_transaction = [util.generate_id()] + view.get_inputs(transactions_data)
        print(new_transaction), 
        correct = view.get_input("Are these data correct? (y/n): ")
        if correct.lower() in ['y', 'yes']:
            list_of_transactions.append(new_transaction)
            continue_adding = view.get_input("Do you want to add another transaction? (y/n): ")
    
    sales.write_table(list_of_transactions)
    view.print_message("A new employee has been added")
    # view.print_error_message("Not implemented yet.")


def update_transaction():
    list_of_transactions = sales.read_table()
    view.print_table(list_of_transactions)
    id_transaction_index = sales.HEADERS.index("Id")
    transaction_data = sales.HEADERS[1:]
    found_ID = False

    while not found_ID:
        transaction_id = view.get_input("Enter the transaction ID: ")
        for transaction in list_of_transactions[1:]:
            if transaction_id == transaction[id_transaction_index]:
                transaction[1:] = view.get_inputs(transaction_data)
                view.print_message("Transaction has been updated.")
                found_ID = True
        if not found_ID:
            view.print_error_message("The ID provided matches no transaction.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_ID = True

    sales.write_table(list_of_transactions)


def delete_transaction():
    list_of_transactions = sales.read_table()
    view.print_table(list_of_transactions)
    found_ID = False
    ID_index = sales.HEADERS.index("Id")

    while not found_ID:
        transaction_id = view.get_input("Please, enter the transaction ID number: ")
        for transaction in list_of_transactions[1:]:
            if transaction[ID_index] == transaction_id:
                list_of_transactions.remove(transaction)
                view.print_message(f"Transaction with id {transaction_id} has been deleted.")
                found_ID = True
        if not found_ID:
            view.print_error_message("The ID provided matches no transaction.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_ID = True

    sales.write_table(list_of_transactions)
    view.press_enter()
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    list_of_transactions = sales.read_table()
    price_index = sales.HEADERS.index("Price")
    biggest_revenue_transaction = list_of_transactions[1]

    for transaction in list_of_transactions[1:]:
        if transaction[price_index] > biggest_revenue_transaction[price_index]:
            biggest_revenue_transaction = transaction
    table = [list_of_transactions[0], biggest_revenue_transaction]
    view.print_message("The transaction that made the biggest revenue")
    view.print_table(table)
    view.press_enter()
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
