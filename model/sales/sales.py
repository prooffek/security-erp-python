""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def read_table():

    table = data_manager.read_table_from_file(DATAFILE)
    table.insert(0, HEADERS)

    return table


def write_table(table):

    data_manager.write_table_to_file(DATAFILE, table[1:])
