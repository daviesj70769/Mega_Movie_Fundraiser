Profit = 0

name = ""
while name != "xxx":

    name = input("Name: ") # replace with function call

    # If name is exit code, break out of loop
    if name == "xxx":
        break

    age = int(input("Age: "))  # replace with function

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made