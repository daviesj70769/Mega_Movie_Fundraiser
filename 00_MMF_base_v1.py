# import statements


# functions go here

# checks that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (& repeat loop)
        else:
            print(error_message)
            print()


# *********** Main Routine **********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# loop to get ticket details

# Get name (can't be blank)
name = not_blank("Name: ", "sorry - this can't be blank, "
                 "please enter your Name")

# Get age (between 12 and 130)

# Calculate ticket price

# Loop to ask for snacks

# Calculate snack price

# ask for payment method (and apply surcharge if necesary)


# Calculate Total sales profit

# Output data to text file
