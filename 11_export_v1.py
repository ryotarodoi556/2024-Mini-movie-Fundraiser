import pandas as pd
import random
from datetime import date

# Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

# Create a dictionary for the DataFrame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

# Create DataFrame
mini_movie_frame = pd.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose a winner from our name list
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index before printing
mini_movie_frame = mini_movie_frame.set_index('Name')

# Get today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Create heading and filename
heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Convert DataFrame to string for export to file
mini_movie_string = mini_movie_frame.to_string()

# Create strings for printing
ticket_costs_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

# Raffle winner announcement
sales_status = "\n--- Raffle Winner ---"
winner_text = "The winner of the raffle is {}. They have won ${:.2f}. ie: Their ticket is free!".format(winner_name, total_won)

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_costs_heading, total_ticket_sales, total_profit, sales_status, winner_text]

# Print output
for item in to_write:
    print(item)

# Write output to file
write_to = "{}.txt".format(filename)
with open(write_to, "w+") as text_file:
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Apply currency formatting
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

print()
print('--- Raffle Winner ---')
print(f"Congratulations {winner_name}. You have won ${total_won:.2f} i.e., your ticket is free!")