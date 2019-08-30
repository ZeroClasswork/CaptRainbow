# CREATE CHECKLIST
checklist = list()

# CREATE RUNNING BOOLEAN
running = True

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
    try:
        # Create item
        if (function_code == "A") | (function_code == "a"):
            input_item = user_input("Add to list:")
            create(input_item)

        # Read item
        elif (function_code == "R") | (function_code == "r"):
            item_index = int(user_input("Which item?\n"))
            print(read(item_index))
        
        # Destroy item
        elif (function_code == "D") | (function_code == "d"):
            item_index = int(user_input("Which item to destroy?\n"))
            destroy(item_index)
            
        # Print all items
        elif (function_code == "P") | (function_code == "p"):
            list_all_items()

        # Update item
        elif (function_code == "U") | (function_code == "u"):
            item_index = int(user_input("What item to update?\n"))
            update_item = user_input("What to update it to?\n")
            update(input_item, update_item)

        # Check item
        elif (function_code == "C") | (function_code == "c"):
            item_index = int(user_input("What item to complete? \n"))
            if item_index < len(checklist):
                if checklist[item_index][0] != "√":
                    mark_completed(item_index)
                else:
                    print("You've already completed that item")
            else:
                print("Invalid input")

        # Quit function
        elif (function_code == "Q") | (function_code == "q"):
            return False

        # Catch all
        else:
            print("Invalid input.")

    except:
        print("Invalid input.")

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
        "Press A to Add to list, R to Read item, D to Destroy item, U to Update item,\n C to mark as Completed, P to show the list, and Q to Quit\n"
    )
    if not select(selection):
        running = False

