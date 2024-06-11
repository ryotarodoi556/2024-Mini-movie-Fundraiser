import math


# integer that is more than zero. Takes in custom error message
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


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# main routine goes here
to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 1)
    print("${:.2f} --> ${:.2f}".format(item, rounded))

# main routine goes here
how_many = num_check("How many items? ", "Can't be 0", int)
total = num_check("Total Costs? ", "More than 0", float)
profit_goal = num_check("profit Goal? ", "More than 0", float)
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))





