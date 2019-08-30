# CREATE CHECKLIST
checklist = list()

# DEFINE FUNCTIONS
# create


def create(item):
    checklist.append(item)

# read


def read(index):
    return checklist[index]

# update


def update(index, item):
    checklist[index] = item

# destroy


def destroy(index):
    checklist.pop(index)

# mark items as completed


def mark_completed(index):
    checklist[index] = "√ " + checklist[index]

# recieve input from user


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# select items based on user input


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Quit function
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")

# print items


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + ": " + list_item)
        index += 1


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    destroy(0)

    list_all_items()

    # Call function with "P" value
    print("select('P'):")
    select("P")
    # Compare results
    print("View items:")
    list_all_items()

    # Call select function "C" value
    print("select('C'):")
    select("C")
    # View results
    print("View items:")
    list_all_items()

    # Call function with "R" value
    print("select('R'):")
    select("R")
    # View results
    print("View items:")
    list_all_items()

    # Call function with "P" value
    print("select('P'):")
    select("P")
    # Compare results
    print("View items:")
    list_all_items()

    # Call function with invalid value
    print("select('U'):")
    select("U")
    # View results
    print("View items:")
    list_all_items()

# test()


running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list"
    )
    select(selection)
