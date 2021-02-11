#  Functions go here


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response

        else:
            print("sorry - this can't be blank, "
                 "please enter your Name")




# Main Routine goes here
name = not_blank("Name: ")
