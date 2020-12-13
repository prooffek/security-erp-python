""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_hr_table_from_file():

    table = [HEADERS]
    [table.append(row) for row in data_manager.read_table_from_file(DATAFILE)]

    return table


def write_hr_table_to_file(table):

    data_manager.write_table_to_file(DATAFILE, table[1:])
