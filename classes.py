import csv

class Customer:
    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.last_name = ""
        self.job_title = ""

    def load_from_csv_row(self, row):
        '''
        Loads data from the specified row in to the instance variables of the object.
        '''
        self.id = row[0]
        self.first_name = row[1]
        self.last_name = row[2]
        self.job_title = row[3]

class CustomerTerminalPrinter:
    def display_customer(self, customer):
        '''
        Prints the properties of the specified Customer object to the terminal.
        '''
        print("ID: " + customer.id)
        print("First Name: " + customer.first_name)
        print("Last Name: " + customer.last_name)
        print("Job Title: " + customer.job_title)

class CustomerList:
    def __init__(self):
        self.customers = []

    def load_from_csv(self, filename):
        '''
        Loads a CSV file containing a list of customer data.
        '''
        # Load the data...
        with open(filename) as file:
            reader = csv.reader(file)

            # Iterate over each row of data in the CSV file.
            for row in reader:

                # Create an instance of a Customer class, using the current rows data.
                customer = Customer()
                customer.load_from_csv_row(row)

                self.customers.append(customer)

    def display_customers(self):
        '''
        Iterates over all the customers in this list, and displays them in the terminal.
        '''
        printer = CustomerTerminalPrinter()
        
        for customer in self.customers:
            printer.display_customer(customer)

#---------------------------------------------------------------------------------------

print("Loading CSV file...\n\n")

customer_list = CustomerList()

customer_list.load_from_csv("D:\\CodeDump\\classes\\Customers.csv")

customer_list.display_customers()

print("\n\nFinished.")
