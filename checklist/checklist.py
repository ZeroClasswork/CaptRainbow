# IMPORTS FOR CHECKING OS TO CLEAR SCREEN
import subprocess, platform

# IMPORT TO USE RNG
import random

# CREATE CHECKLIST
checklist = list()

# CREATE RUNNING BOOLEAN
running = True

# CREATING RAINBOW OF TEXT OPTIONS
END = "\33[0m"
ALTEND = "\33"
RED = "\33[31m"
YELLOW = "\33[33m"
GREEN = "\33[32m"
BLUE = "\33[34m"
VIOLET = "\33[35m"
GREY = "\33[90m"
rainbow = [RED, YELLOW, GREEN, BLUE, VIOLET]

# DEFINE FUNCTIONS
# create


def create(item):
    color = random.choice(rainbow)
    checklist.append(color + "  " + item + END)

# read


def read(index):
    return checklist[index]

# update


def update(index, item):
    checklist[index] = str(checklist[index][0:2]) + item

# destroy


def destroy(index):
    checklist.pop(index)

# mark items as completed


def mark_completed(index):
    if checklist[index][0] == "√":
        checklist[index] = " " + str(checklist[index][1:])
    elif checklist[index][0] != "√":
        checklist[index] = YELLOW + "√" + ALTEND + str(checklist[index][1:])


# print items


def list_all_items():
    index = 0
    if len(checklist) > 0:
        for list_item in checklist:
            color = random.choice(rainbow)
            print(color + str(index) + ": " + str(list_item) + END)
            index += 1

    else:
        print(GREY + "Nothing to display." + END)

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
            input_item = user_input(RED + "Add to list:" + END)
            create(input_item)

        # Read item
        elif (function_code.upper() == "R"):
            item_index = int(user_input(YELLOW + "Which item?\n" + END))
            print(RED + str(item_index) + GREYBG + ": " + END + read(item_index) + END)
            
            user_response = "no"
            while not ((user_response.upper() == "Y") or (user_response.upper() == "YES")):
                user_response = user_input(GREY + "Continue?\n" + END)

        # Destroy item
        elif (function_code.upper() == "D"):
            item_index = int(user_input(GREEN + "Which item to destroy?\n" + END))
            destroy(item_index)

        # Print all items
        elif (function_code.upper() == "P"):
            list_all_items()
            user_response = "no"
            while not ((user_response.upper() == "Y") or (user_response.upper() == "YES")):
                user_response = user_input(GREY + "Continue?\n" + END)

        # Update item
        elif (function_code.upper() == "U"):
            item_index = int(user_input(BLUE + "What item to update?\n" + END))
            while item_index >= len(checklist):
                print(GREY + "Invalid input." + END )
                item_index = int(user_input(BLUE + "What item to update?\n" + END))
            update_item = user_input(BLUE + "What to update it to?\n" + END)
            update(item_index, update_item)

        # Check item
        elif (function_code.upper() == "C"):
            item_index = int(user_input(VIOLET + 
                "What item to complete / uncomplete? \n" + END))
            if item_index < len(checklist):
                mark_completed(item_index)
            else:
                print(GREEN + "Invalid input" + END)

        # Quit function
        elif (function_code.upper() == "Q"):

            if platform.system() == "Windows":  # Windows
                subprocess.Popen("cls", shell=True).communicate()
            else:                               # Linux and Mac
                print("\033c", end="")

            return False

        # Catch all
        else:
            print(GREY + "Invalid input." + END)

            user_response = "no"
            while not ((user_response.upper() == "Y") or (user_response.upper() == "YES")):
                user_response = user_input(GREY + "Continue?\n" + END)

        if platform.system() == "Windows":  # Windows
            subprocess.Popen("cls", shell=True).communicate()
        else:                               # Linux and Mac
            print("\033c", end="")

        return True

    except:
        print("Invalid input.")

        user_response = "no"
        while not ((user_response.upper() == "Y") or (user_response.upper() == "YES")):
            user_response = user_input(GREY + "Continue?\n" + END)

        if platform.system() == "Windows":  # Windows
            subprocess.Popen("cls", shell=True).communicate()
        else:                               # Linux and Mac
            print("\033c", end="")

        return True

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
        RED + "Press A to Add to list," + YELLOW + " R to Read item, " + 
        GREEN + " D to Destroy item," + BLUE + " U to Update item,\n " + 
        VIOLET + "C to mark as Completed / unCompleted," +
        GREY + " P to show the list, and Q to Quit\n" + END
    )

    if not select(selection):
        running = False
