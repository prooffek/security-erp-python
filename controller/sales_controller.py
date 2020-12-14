from model.sales import sales
from view import terminal as view
from model import util
from datetime import datetime


def list_transactions():

    view.print_message("List of transactions:\n")
    view.print_table(sales.read_table())
    view.get_input("Press ENTER to return to MAIN MENU")


def add_transaction():

    list_of_transactions = sales.read_table()
    transactions_data = sales.HEADERS[1:]
    continue_adding = "y"

    while continue_adding.lower() in ["y", "yes"]:
        new_transaction = [util.generate_id()] + view.get_inputs(transactions_data)
        view.print_message(new_transaction)
        view.print_message("Succesfully added new transaction.")
        correct = view.get_input("Are these data correct? (y/n): ")
        if correct.lower() in ['y', 'yes']:
            list_of_transactions.append(new_transaction)
            continue_adding = view.get_input("Do you want to add another transaction? (y/n): ")

    sales.write_table(list_of_transactions)
    view.get_input("Press ENTER to return to MAIN MENU")


def update_transaction():

    list_of_transactions = sales.read_table()
    view.print_table(list_of_transactions)
    id_transaction_index = sales.HEADERS.index("Id")
    transaction_data = sales.HEADERS[1:]
    found_ID = False

    while not found_ID:
        transaction_id = view.get_input("Enter the transaction ID number: ")
        for transaction in list_of_transactions[1:]:
            if transaction_id == transaction[id_transaction_index]:
                transaction[1:] = view.get_inputs(transaction_data)
                view.print_message(f"Transaction with id {transaction_id} has been updated.")
                found_ID = True
        if not found_ID:
            view.print_error_message("The ID provided matches no transaction.")
            user_input = view.get_input("Do you want to enter a different ID? (y/n): ")
            if user_input.lower() in ["n", "no"]:
                found_ID = True

    sales.write_table(list_of_transactions)
    view.get_input("Press ENTER to return to MAIN MENU")


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
    view.get_input("Press ENTER to return to MAIN MENU")


def get_biggest_revenue_transaction():

    list_of_transactions = sales.read_table()
    price_index = sales.HEADERS.index("Price")
    biggest_revenue_transaction = list_of_transactions[1]
    for transaction in list_of_transactions[1:]:
        if float(transaction[price_index]) > float(biggest_revenue_transaction[price_index]):
            biggest_revenue_transaction = transaction
    table = [sales.HEADERS, biggest_revenue_transaction]
    view.print_message("The transaction that made the biggest revenue")
    view.print_table(table)
    view.get_input("Press ENTER to return to MAIN MENU")


def get_biggest_revenue_product():

    list_of_transactions = sales.read_table()
    price_index = sales.HEADERS.index("Price")
    name_index = sales.HEADERS.index("Product")
    first_product = list_of_transactions[1][name_index]
    product_revenue_dict = {}

    for transaction in list_of_transactions[1:]:
        if transaction[name_index] not in product_revenue_dict:
            product_revenue_dict[transaction[name_index]] = float(transaction[price_index])
        else:
            product_revenue_dict[transaction[name_index]] += float(transaction[price_index])

    biggest_revenue = product_revenue_dict[first_product]
    product_with_biggest_revenue = first_product

    for key, value in product_revenue_dict.items():
        if value > biggest_revenue:
            biggest_revenue = value
            product_with_biggest_revenue = key

    table = [sales.HEADERS]

    for transaction in list_of_transactions[1:]:
        if transaction[name_index] == product_with_biggest_revenue:
            table.append(transaction)

    view.print_message(f"The product with the biggest revenue is: {product_with_biggest_revenue}\nThe revenue of the product is: {product_revenue_dict[product_with_biggest_revenue]}")
    view.print_message("/n")
    view.print_table(table)

    view.get_input("Press ENTER to return to MAIN MENU")


def count_transactions_between():

    list_of_transaction = sales.read_table()
    date_index = sales.HEADERS.index("Date")
    dates = ["Enter beginning date in format YYYY-MM-DD: ", "Enter final date in format YYYY-MM-DD: "]
    beginning_date, final_date = view.get_inputs(dates)
    beginning_date = datetime.strptime(beginning_date, "%Y-%m-%d")
    final_date = datetime.strptime(final_date, "%Y-%m-%d")
    number_of_transaction = 0
    for transaction in list_of_transaction[1:]:
        transaction_date = datetime.strptime(transaction[date_index], "%Y-%m-%d")
        if transaction_date >= beginning_date and transaction_date <= final_date:
            number_of_transaction += 1

    view.print_general_results(number_of_transaction, "Number of transactions between two given dates")
    view.get_input("Press ENTER to return to MAIN MENU")


def sum_transactions_between():
    list_of_transactions = sales.read_table()
    date_index = sales.HEADERS.index("Date")
    price_index = sales.HEADERS.index("Price")
    dates = ["Enter beginning date in format YYYY-MM-DD: ", "Enter final date in format YYYY-MM-DD: "]
    beginning_date, final_date = view.get_inputs(dates)
    beginning_date = datetime.strptime(beginning_date, "%Y-%m-%d")
    final_date = datetime.strptime(final_date, "%Y-%m-%d")

    transaction_sum = 0
    table = [sales.HEADERS]
    for transaction in list_of_transactions[1:]:
        transaction_date = datetime.strptime(transaction[date_index], "%Y-%m-%d")
        if transaction_date >= beginning_date and transaction_date <= final_date:
            transaction_sum += float(transaction[price_index])
            table.append(transaction)

    view.print_general_results(transaction_sum, f"The sum of trunsactions completed between {beginning_date} and {final_date} is")
    view.print_table(table)
    view.get_input("Press ENTER to return to MAIN MENU")


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
