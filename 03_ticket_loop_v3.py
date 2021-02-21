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
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("you have sold all the available tickets!")
else:
    print("you have sold {} tickets.  \n"
         "there are {} places still available"
         .format (count, MAX_TICKETS - count))
