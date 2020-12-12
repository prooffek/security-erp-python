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
    print()
    view.print_table(table)
    
    view.press_enter()

    #view.print_error_message("Not implemented yet.")


def count_transactions_between():

    list_of_transactions = sales.read_table()
    date_index = sales.HEADERS.index("Date")
    separator = "-"
    dates = ["baginning date", "final date"]

    print("Please provide the baginning and final dates.\n") #ask the user about the range of transactions dates
    beginning_date, final_date = view.get_inputs(dates)
    beginning_year, beginning_month, beginning_day = beginning_date.split(separator)
    final_year, final_month, final_day = final_date.split(separator)
    number_of_transaction = 0
    
    for transaction in list_of_transactions[1:]: #Comparing the transaction date with the dates provided by the user
        transaction_year, transaction_month, transaction_day = transaction[date_index].split(separator)
        if int(transaction_year) >= int(beginning_year) and int(transaction_year) <= int(final_year):
            if int(transaction_month) >= int(beginning_month) and int(transaction_month) <= int(final_month):
                if int(transaction_day) >= int(beginning_day) and int(transaction_day) <= int(final_day):
                    number_of_transaction += 1

    view.print_general_results(int(number_of_transaction), f"Number ofnumber of transactions between {beginning_date} and {final_date} is")
    view.press_enter()


def sum_transactions_between():
    list_of_transactions = sales.read_table()
    date_index = sales.HEADERS.index("Date")
    price_index = sales.HEADERS.index("Price")
    separator = "-"
    dates = ["baginning date", "final date"]

    print("Please provide the baginning and final dates.\n") #ask the user about the range of transactions dates
    beginning_date, final_date = view.get_inputs(dates)
    beginning_year, beginning_month, beginning_day = beginning_date.split(separator)
    final_year, final_month, final_day = final_date.split(separator)

    transaction_sum = 0
    table = [sales.HEADERS]

    for transaction in list_of_transactions[1:]: #Comparing the transaction date with the dates provided by the user
        value = False
        transaction_year, transaction_month, transaction_day = transaction[date_index].split(separator)
        if int(transaction_year) > int(beginning_year) and int(transaction_year) < int(final_year):
            value = True
        elif int(transaction_year) == int(beginning_year) and int(transaction_month) >= int(beginning_month) and int(transaction_day) >= int(beginning_day) and int(transaction_year) <= int(final_year) and int(transaction_month) <= int(final_month) and int(transaction_day) <= int(final_day):
            value = True
        elif int(transaction_year) >= int(beginning_year) and int(transaction_month) >= int(beginning_month) and int(transaction_day) >= int(beginning_day) and int(transaction_year) == int(final_year) and int(transaction_month) <= int(final_month) and int(transaction_day) <= int(final_day):
            value = True
        
        if value:
            transaction_sum += float(transaction[price_index])
            table.append(transaction)

    view.print_general_results(transaction_sum, f"The sum of trunsactions completed between {beginning_date} and {final_date} is")
    view.print_table(table)
    view.press_enter()
    #view.print_error_message("Not implemented yet.")


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
