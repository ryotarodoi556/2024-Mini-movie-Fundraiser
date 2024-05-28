import pandas as pd
import random
from datetime import date

# Function to check if the user has entered 'yes' or 'no'
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no")

# Function to ensure the user input is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print("Sorry this can't be blank. Please try again")

# Function to check if the user input is a valid integer
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")

# Function to calculate the ticket price based on the age
def calc_ticket_price(age):
    if age < 16:
        return 7.5
    elif age < 65:
        return 10.5
    else:
        return 6.5

# Function to check if the user input is within a set of valid responses
def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in (item[:num_letters], item):
                return item
        print(error)

# Function to format currency values
def currency(x):
    return "${:.2f}".format(x)

# Main routine
MAX_TICKETS = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

all_names = []
all_ticket_costs = []
all_surcharge = []

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

if want_instructions == "yes":
    print("Instructions go here")
print()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

    if not (12 <= age <= 120):
        if age < 12:
            print("Sorry, you are too young for this movie")
        else:
            print("?? That looks like a typo, please try again.")
        continue

    ticket_cost = calc_ticket_price(age)
    pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)

    surcharge = 0 if pay_method == "cash" else ticket_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

mini_movie_frame = pd.DataFrame(mini_movie_dict)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

winner_name = random.choice(all_names)
total_won = mini_movie_frame.loc[mini_movie_frame['Name'] == winner_name, 'Total'].values[0]

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for item in add_dollars:
    mini_movie_frame[item] = mini_movie_frame[item].apply(currency)

mini_movie_frame = mini_movie_frame.set_index('Name')

today = date.today()
heading = f"---- Mini Movie Fundraiser Ticket Data ({today.strftime('%d/%m/%Y')}) ----\n"
filename = f"MMF_{today.strftime('%Y_%m_%d')}.txt"

mini_movie_string = mini_movie_frame.to_string()

ticket_costs_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = f"Total Ticket Sales: ${total:.2f}"
total_profit = f"Total Profit: ${profit:.2f}"

if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = "\n **** You have sold {} out of {} " \
                   "tickets *****".format(tickets_sold, MAX_TICKETS)


winner_heading = "\n--- Raffle Winner ---"
winner_text = f"The winner of the raffle is {winner_name}. They have won ${total_won:.2f}. ie: Their ticket is free!"

to_write = [heading, mini_movie_string, ticket_costs_heading, total_ticket_sales, total_profit, sales_status, winner_heading, winner_text]

for item in to_write:
    print(item)

with open(filename, "w") as text_file:
    for item in to_write:
        text_file.write(item + "\n")
