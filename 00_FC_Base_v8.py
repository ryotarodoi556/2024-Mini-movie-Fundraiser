# import libraries
import math
import pandas


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

# gets expenses, returns list which has the data frame and sub total

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

# prints expense frames

def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

def profit_goal(total_costs):
    # initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:
        # ask for profit goal...
        response = input("What is your profit goal (e.g., $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

            if profit_type == "unknown" and amount >= 100:
                dollar_type = yes_no("Do you mean ${:.2f} (i.e., {:.2f} dollars)? y/n: ".format(amount, amount))

                # set profit type based on user answer above
                if dollar_type == "yes":
                    profit_type = "$"
                else:
                    profit_type = "%"

            elif profit_type == "unknown" and amount < 100:
                percent_type = yes_no("Do you mean {}%? y/n: ".format(amount))
                if percent_type == "yes":
                    profit_type = "%"
                else:
                    profit_type = "$"

            # return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal

        except ValueError:
            print(error)

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# main routine goes here
to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 1)
    print("${:.2f} --> ${:.2f}".format(item, rounded))
# main routine goes here
all_costs = 200

# loop for quick testing
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()


# *** main routine goes here ***
# get product name
product_name = not_blank("Product name: ", "The product name can't be blank")

how_many = num_check("How many items wil you be producing? ",
                     "The number of items must be whole "
                     "number more than zero", int)

print()
print("Please enter your variable costs below...")

# get variable cost
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":
    # get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = variable_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0


# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask user for rounding
round_to = num_check("Round to nearest...? $",
                     "Can't be 0", int)

# calculate recommended price
selling_price = sales_needed / how_many
print("Selling Price (unrounded):"
      " ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)

# write data to file

# *** printing area ***
print()
print("**** Fund Raising - {} *****".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

    print()
    print("**** Total Costs: ${:.2f} ****".format(all_costs))
    print()

    print()
    print("**** Profit & Sales Targets ****")
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))

    print()
    print("**** Pricing ****")
    print("Minimum Price: ${:.2f}".format(selling_price))
    print("**** Recommended Selling Price: ${:.2f}".format(selling_price))



