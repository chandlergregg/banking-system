from os import path
from os import remove
import csv

def init_customer_csv(filename):
    """
    Initializes csv by deleting filename (if exists), 
    setting headers, and adding mock customer info
    """

    # Clear out file if it already exists
    if path.exists(filename):
        remove(filename)

    # Set headers and data
    headers = ["first_name", "last_name", "email_address", "password", "tel_number"]
    data = [["Ada", "Lovelace", "alovelace@gmail.com", "alovelace123", "None"],
            ["Grace", "Hopper", "ghopper@hotmail.com", "ghopper456", "None"],
            ["Edith", "Clarke", "eclarke@yahoo.com", "eclark789", "None"],
            ["Carol", "Shaw", "cshaw@aol.com", "cshaw123", "None"]]

    # Write headers, data
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(data)

init_customer_csv("pybank_customers.csv")