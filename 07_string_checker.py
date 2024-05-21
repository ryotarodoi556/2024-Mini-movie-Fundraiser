# check that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print("Please enter a valid response")


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the "
                                       "instructions (y/n): ",
                                       1, yes_no_list)
    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("...",
                                2, payment_list)
    print("you chose", pay_method)

