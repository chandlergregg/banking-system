from csv import writer

class Customer:

    def __init__(self, first_name, last_name,
                 email_address, password, tel_number=None):

        # Initialize variables
        self.first_name     = first_name
        self.last_name      = last_name
        self.email_address  = email_address
        self.password       = password
        self.tel_number     = tel_number

    def save_to_csv(self, filename):

        # Set data and filename for writing
        data = [self.first_name, self.last_name, self.email_address,
                self.password, self.tel_number]

        # Write to csv
        with open(filename, "a") as csvfile:
            csv_writer = writer(csvfile)
            csv_writer.writerow("\n")
            csv_writer.writerow(data)

    def __repr__(self):

        return (
            f"\nCustomer details:\n"
            f"-----------------------------\n"
            f"First name:       {self.first_name}\n"
            f"Last name:        {self.last_name}\n"
            f"Email address:    {self.email_address}\n"
            f"Password:         {self.password}\n"
            f"Telephone number: {self.tel_number}\n"
        )
