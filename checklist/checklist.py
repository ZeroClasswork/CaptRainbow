# IMPORTS FOR CHECKING OS TO CLEAR SCREEN
import subprocess, platform

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
        if (function_code.upper() == "A"):
            input_item = user_input("Add to list:")
            create(input_item)

        # Read item
        elif (function_code.upper() == "R"):
            item_index = int(user_input("Which item?\n"))
            print(read(item_index))
            user_response = "no"
            while not ((user_response.upper() == "Y") | (user_response.upper() == "YES")):
                user_response = user_input("Continue?")
        
        # Destroy item
        elif (function_code.upper() == "D"):
            item_index = int(user_input("Which item to destroy?\n"))
            destroy(item_index)
            
        # Print all items
        elif (function_code.upper() == "P"):
            list_all_items()
            user_response = "no"
            while not ((user_response.upper() == "Y") | (user_response.upper() == "YES")):
                user_response = user_input("Continue?")
                

        # Update item
        elif (function_code.upper() == "U"):
            item_index = int(user_input("What item to update?\n"))
            while item_index >= len(checklist):
                print("Invalid input.")
                item_index = int(user_input("What item to update?\n"))
            update_item = user_input("What to update it to?\n")
            update(input_item, update_item)

        # Check item
        elif (function_code.upper() == "C"):
            item_index = int(user_input("What item to complete? \n"))
            if item_index < len(checklist):
                if checklist[item_index][0] != "√":
                    mark_completed(item_index)
                else:
                    print("You've already completed that item")
            else:
                print("Invalid input")

        # Quit function
        elif (function_code.upper() == "Q"):
            return False

        # Catch all
        else:
            print("Invalid input.")

        if platform.system() == "Windows":  # Windows
            subprocess.Popen("cls", shell=True).communicate()
        else:                               # Linux and Mac
            print("\033c", end="")

        return True

    except:
        print("Invalid input.")

        user_response = "no"
        while not ((user_response.upper() == "Y") | (user_response.upper() == "YES")):
                user_response = user_input("Continue?")

        if platform.system() == "Windows":  # Windows
            subprocess.Popen("cls", shell=True).communicate()
        else:                               # Linux and Mac
            print("\033c", end="")

        return True

# print items
def list_all_items():
    index = 0
    if len(checklist) > 0:
        for list_item in checklist:
            print(str(index) + ": " + list_item)
            index += 1

    else:
        print("Nothing to display.")


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

