""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def get_crm_table_from_file():

    table = [HEADERS]
    [table.append(row) for row in data_manager.read_table_from_file(DATAFILE)]

    return table


def write_crm_table_to_file(table):

    data_manager.write_table_to_file(DATAFILE, table[1:])
 