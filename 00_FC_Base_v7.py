# import libraries


# *** functions go here ***

# checks that input is either a float or an integer that is more than zero. takes in custom error message

def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here
get_int = num_check("How many do you need? ",
                    "Please enter an amount more than 0\n",
                    int)
get_cost = num_check("How much does it cost? $",
                     "PLease enter a number more than 0\n",
                     float)
print("You need: {}".format(get_int))
print("It costs: ${}".format(get_cost))

def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return  var_item

        print("Please enter either yes or no...\n")


# Loops to make testing faster...
for item in range(0,6):
    want_help = yes_no("Do you want to read the instructions? ")
    print("You said '{}'\n".format(want_help))

def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


def currency(x):
    return "${:.2f}".format(x)

def get_expenses(var_fixed):


    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity:",
                             "The amount must be a whole number "
                             "more than zero",
                             int)
        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('item')

    # calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity']\
                             * expense_frame['Price']

    # find sub total
    sub_total = expense_frame['Cost'].sum()


    # currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# *** main routine goes here ***

# get product name
product_name = not_blank("Product name: ", "The product name can't be blank")


# get variable cost
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]


# get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = variable_expenses[0]
fixed_sub = fixed_expenses[1]

# *** printing area ***

print("**** Variable Costs ****")
print(variable_frame)
print()

print("Variable Costs: ${:.2f}".format(variable_sub))

print("**** Fixed Costs ****")
print(fixed_frame[['Cost']])
print()
print("Fixed Costs: ${:.2f}".format(fixed_sub))


