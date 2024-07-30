# Function to check if the user has entered 'yes' or 'no'
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")


# Function to ensure the user input is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response:
            return response
        else:
            print("Sorry, this can't be blank. Please try again.")


# Function to check if the user input is a valid integer
def num_check(question, low, high):

    error = f"Enter a number between {low} and {high}"

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in (item[:num_letters], item):
                return item
        print(error)


# Main routine
yes_no_list = ["yes", "no"]

# List of sneakers and their prices
sneakers = {
    "Rick Owens Geobasket": 900,
    "Maison Margiela Replica": 800,
    "Balenciaga Triple S": 950,
    "Crocs": 50,
    "Vans Knu Skools": 150,
    "Off-White Vulcanized": 650,
    "Alexander McQueen Oversized": 580,
    "Air Force 1": 120,
    "Yeezy Boost 350": 500,
    "Jordan 4": 400,
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to see how to use this price comparison tool? (y/n): ", 1, yes_no_list)

if want_instructions == "yes":
    print("This is a price comparison tool for high-end sneakers available at the store. "
          "\nIt asks how much money you have and gives a list of products that fit the budget. "
          "\nThen it gives a list of sneakers that provide the most value for money.")
    print()

# Get the user's budget
budget = num_check("How much is your budget today?: ", 50, 1000)

# Print the available sneakers within the budget
print("\nHere are the sneakers you can afford with your budget:")
affordable_sneakers = {name: price for name, price in sneakers.items() if price <= budget}

if affordable_sneakers:
    for name, price in affordable_sneakers.items():
        print(f"{name}: ${price}")
else:
    print("Sorry, no sneakers are available within your budget.")

print("\nThank you for using the sneaker price comparison tool! See you later.")
