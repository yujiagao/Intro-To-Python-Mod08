# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# GYJ, 8 Jun 2021: started assignment after hospitalisation
# GYJ, 11 Jun 2021: completed codes for assignment 8
#
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstTable = []
dicrow = {}
strChoice = ""
strStatus = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    # --Constructor--
    def __init__(self, prod_name, price):
        self.__prod_name = prod_name
        self.__prod_price = price

    # -- Properties --
    # Product Name
    @property
    def prod_name(self):  # retrieves product name
        return str(self.__prod_name).title()

    @prod_name.setter
    def prod_name(self, value):  # define product name
        if str(value).isnumeric() == False:
            self.__prod_name == value
        else:
            raise Exception("Names cannot be numbered")

    # Price
    @property
    def prod_price(self):   #retrieve product price
        return str(self.__prod_price)

    @prod_price.setter      #set product price
    def prod_price(self, value):
        try:
            self.__prod_price = value
        except ValueError:
            raise Exception("Please enter numbers")

    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name):   #read data from file into dic rows
        list_of_objects = []
        file = open(strFileName, "r")
        for line in file:
            data = line.split(",")
            prod_name = data[0].strip()
            prod_price = float(data[1].strip())
            list_of_objects.append(Product(prod_name, prod_price))
        file.close()
        return list_of_objects

    @staticmethod
    def add_data_to_list(list_of_objects, prod_name, prod_price): #adds data to dic rows
        list_of_objects.append(Product(prod_name, prod_price))

    @staticmethod
    def remove_data_from_list(list_of_objects, ProdToRemove):
        sucess_status = False
        prod_number = 0
        for Product in list_of_objects:
            if Product.prod_name == ProdToRemove:
                del list_of_objects[prod_number]
                sucess_status = True
            prod_number += 1
        return list_of_objects

    @staticmethod
    def write_data_to_file(file_name, list_of_objects):
        f = open(file_name, "w")
        for Product in list_of_objects:
            f.write(str(Product.prod_name + ',' + Product.prod_price + '\n'))
        f.close()
        print("Data saved")
        return list_of_objects

    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Products():
        print('''
           Menu of Options
           1) Add a new Product 
           2) Remove an existing Product
           3) Save Data to File        
           4) Read Data from File
           5) Exit Program
           ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        try:
            choice = str(input("Please choose an option [1-5] - ")).strip()
        except ValueError:
            print("Please select options 1-5")
        print()
        return choice

    # TODO: Add code to show the current data from the file to user
    def print_current_Products_in_list(lstTable):
        for Product in lstTable:
            print("Product_Name: {}, Product_Price: {}".format(Product.prod_name, Product.prod_price))
            # print(row["Product_Name"] + " (" + row["Product_Price"] + ")")
        print()

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        prod_name = str(input("Enter Product Name: ")).strip()
        prod_price = input("Enter Product Price: ").strip()
        print()
        return prod_name, prod_price

    @staticmethod
    def input_product_to_remove():
        prod_name = str(input("Enter Product to Remove: ")).strip()
        return prod_name

    @staticmethod
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press Enter to continue.')
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstTable = FileProcessor.read_data_from_file(strFileName)

# Show user a menu of options
while (True):
    IO.print_menu_Products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get user's menu option choice
    if strChoice.strip() == '1':  # Adds a New Products
        tplData = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(lstTable, tplData[0], tplData[1])  # Adds Data to List
        IO.print_current_Products_in_list(lstTable)
        print("New Product Added")
        continue  # to show the menu
    elif strChoice == '2':  # Removes an Existing Product
        ProdToRemove = input("Enter Product to Remove: ")
        ItemRemoved = FileProcessor.remove_data_from_list(lstTable, ProdToRemove)
        print("Product Removed")
        continue  # to show the menu

    # let user save current data to file and exit program
    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Enter Y/N to Save Data: ")
        if strChoice.lower() == "y":
            FileProcessor.write_data_to_file(strFileName, lstTable)  # Writes Data to File
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Data Not Saved")
        continue  # to show the menu

    elif strChoice == '4':  # Read Data from File
        strChoice = IO.input_yes_no_choice("Load Data From File? Y/N: ")
        if strChoice.lower() == 'y':
            IO.print_current_Products_in_list(lstTable)
        else:
            IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye")
        break

# Main Body of Script  ---------------------------------------------------- #