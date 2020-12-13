import os
from prettytable import PrettyTable


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{title}:\n")

    for option_index in range(len(list_options)):
        print(f"  ({option_index}) {list_options[option_index]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int or type(result) == float:
        print(f"{label}: %.2f" % result)
    elif type(result) == list or type(result) == tuple:
        print(f"{label}:\n  ", end="")
        [print(item) if item == result[-1] else print(item, end="; ") for item in result]
    elif type(result) == dict:
        print(f"{label}\n  ", end="")
        last_key = list(result.keys())[-1]
        [print(f"{key}: {value}") if key == last_key else print(f"{key}: {value}", end="; ") for key, value in result.items()]


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """

    display_table = PrettyTable()
    display_table.field_names = table[0]
    row_index = 1

    while row_index < len(table):
        display_table.add_row(table[row_index])
        row_index += 1

    print(display_table)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label + "\n")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs_user = []

    for label_index in range(len(labels)):
        user_input = input(labels[label_index] + "\n")
        inputs_user.append(user_input)

    return inputs_user


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
