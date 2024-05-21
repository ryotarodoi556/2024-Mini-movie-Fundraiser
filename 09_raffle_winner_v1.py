import pandas as pd
import random

# Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pd.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in list
win_index = all_names.index(winner_name)

# Look up total amount won (i.e., ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print('--- Raffle Winner ---')
print(f"Congratulations {winner_name}. You have won ${total_won:.2f} i.e., your ticket is free!")

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("----- Ticket Data ------")
print()

# Output table with ticket data
print(mini_movie_frame)

print()
print("------ Ticket Cost / Profit -------")

# Output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")