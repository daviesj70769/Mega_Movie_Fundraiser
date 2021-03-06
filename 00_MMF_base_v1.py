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


# Checks for an integer more than 0
def int_check(question):

    error = "please enter a whole number that is more than "

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# *********** Main Routine **********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# loop to get ticket details

#start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
       print("you have {} seats "
             "left".format(MAX_TICKETS - count))

    # Warns user that only one seat is left!
    else:
        print("*** There is One seat left!! ***")

    # Get details...

    # Get name loop (cant be blank)
    name = not_blank("What is your name:", "sorry - this can't be blank, "
                     "please enter your Name:")

    # End the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # Check that age is valid...
    if age < 12:
        print ("sorry you are too young for this movie")
        continue
    elif age >130:
        print("That is very old - it lookis like a mistake")
        continue

    count += 1


# End of tickets loop

# Calculate profit etc...

if count == MAX_TICKETS:
    print("you have sold all the available tickets!")
else:
    print("you have sold {} tickets.  \n"
          "there are {} places still available".format(count, MAX_TICKETS - count))


# Get age (between 12 and 130)

# Calculate ticket price

# Loop to ask for snacks

# Calculate snack price

# ask for payment method (and apply surcharge if necesary)


# Calculate Total sales profit

# Output data to text file
