# tabulate module to organise data
from tabulate import tabulate

# =========The beginning of the class==========
# Create class with given attributes
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define get_cost method
    def get_cost(self):
        return self.cost

    # define get_quantity method
    def get_quantity(self):
        return self.quantity

    # method to update quantity/re_stock
    def add_to_quantity(self, quantity):
        self.quantity += quantity

    # string methid to return string representation of class
    def __str__(self):
        return f"\nProduct: {self.product}\nCost: R{self.cost}\t\tQuantity: {self.quantity}\t\tCode: {self.code}\t\tCountry: {self.country}"


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
# ==========Functions outside the class==============

# define read_shoes_data function 
# reads from file inventory.txt
def read_shoes_data():
    inventory_f = open("inventory.txt", "r")
    data = inventory_f.readlines()

    # for loop to iterate over each position in each line
    for pos, line in enumerate(data, 1):
        if pos == 1:
            continue
        # split the data and strip away new lines, commas and spaces
        split_data = line.strip("\n").split(",")
        # try/except to catch errors
        try:
            shoe = Shoe(split_data[0], split_data[1], split_data[2], float(split_data[3]), float(split_data[4]))
            shoe_list.append(shoe)
        except:
            print(f"Unable to parse shoe data: {split_data}")
    # message confirming data has been read
    print("Inventory data read successfully")

# define write_shoe_data function
# writes to file inventory.txt
def write_shoe_data():
    inventory_f = open("inventory.txt", "w")

    # create headers
    inventory_f.write("Country,Code,Product,Cost,Quantity\n")
    # write shoe information to inventory.txt
    for i in range(len(shoe_list)):
        inventory_f.write(f"{shoe_list[i].country},{shoe_list[i].code},{shoe_list[i].product},{shoe_list[i].cost},{shoe_list[i].quantity}\n")

# define capture_shoes function
# user can input information about the shoe
# information appended to list
def capture_shoes():
    country = input("Please enter the country of the shoe: ")
    code = input("Please enter the SKU code of the shoe: ")
    product = input("Please enter the product name of the shoe: ")
    cost = float(input("Please enter the cost of the shoe: "))
    quantity = float(input("Please enter the inventory quantity of the shoe: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

# define view_all function
def view_all():
    # initialise list for tabulated data
    table = []

    # iterate over shoes list
    for i in range(len(shoe_list)):
        row = [shoe_list[i].country, shoe_list[i].code, shoe_list[i].product, shoe_list[i].cost, shoe_list[i].quantity]
        table.append(row)
    # print details of the shoes
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

# define re_stock function
# if no items on list, print error message
def re_stock():
    if len(shoe_list) == 0:
        print("No shoe data exists, please load the inventory")
        return 
    
    # conditional statements to find lowest quantity product and print item
    index = 0
    for i in range(len(shoe_list)):
        if i == 0 or shoe_list[i].get_quantity() < shoe_list[index].get_quantity():
            index = i
    print(f"The following shoe has the lowest quantity of stock:\n{shoe_list[index]}")
    # request quantity to add
    quantity = float(input("Please enter the quantity you wish to add for the shoe: "))
    # call add_to_quantity function
    shoe_list[index].add_to_quantity(quantity)
    # print message to user
    print(f"The quantity for the shoe has been updated:\n{shoe_list[index]}")
    # call write_shoe_data function to update file
    write_shoe_data()

# define search_shoe function
def search_shoe():
    # request code from user
    code = input("Please enter the SKU code of the shoe to search for: ")
    
    # itterate over list to search for code
    for i in range(len(shoe_list)):
        if shoe_list[i].code == code:
            return shoe_list[i]
    # print error message
    print(f"Shoe not found for code {code}")

# define value_per_item function
def value_per_item():
    # error message for no data
    if len(shoe_list) == 0:
        print("No shoe data exists, please load the inventory")
        return
    
    # itterate over list to calculate total value peritem
    for i in range(len(shoe_list)):
        value = shoe_list[i].get_quantity() * shoe_list[i].get_cost()
        # print amount
        print(f"{shoe_list[i]}\t\tTotal Value: R{value}")

# define highest_qty function
def highest_qty():
    # error message
    if len(shoe_list) == 0:
        print("No shoe data exists, please load the inventory")
        return 

    # find item with highest quantity
    index = 0
    for i in range(len(shoe_list)):
        if i == 0 or shoe_list[i].get_quantity() > shoe_list[index].get_quantity():
            index = i
    # print sale message
    print(f"The following shoe is for sale:\n{shoe_list[index]}")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''\nSelect one of the following Options below:
    r - \tRead shoes data
    a - \tAdd new shoe data
    v - \tView shoe data
    l - \tRestock the show with the lowest quantity
    s - \tSearch for shoe
    c - \tCalculate shoe value
    h - \tSearch for shoe with the highest quantity
    e - \tExit
    : ''').lower()

    if menu == 'r':
        read_shoes_data()

    elif menu == 'a':
        capture_shoes()

    elif menu == 'v':
        view_all()

    elif menu == 'l':
        re_stock()

    elif menu == 's':
        shoe = search_shoe()
        if shoe != None:
            print(shoe)

    elif menu == 'c':
        value_per_item()

    elif menu == 'h':
        highest_qty()
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")