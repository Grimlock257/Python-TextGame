######################################################
# This version is hard coded via functions
######################################################

# Game play variables
inventory = []
name = ""


def get_string_input(question, choices):
    """ Get string input from user """
    # Display questions and valid answers
    print(question)
    if choices != "*":
        for i in range(len(choices)):
            print(str(i + 1) + ") " + choices[i])

    while True:
        choice = str(input("\n> ")).upper()

        # Make sure user input choice is in the valid choices, else tell them it's not and restart loop
        if choice in choices or choices == "*":
            return choice
        else:
            print("That is not a valid choice! Choose from:", ", ".join(choices))


def get_integer_input(question, choices):
    """ Get integer input from user, making sure the input is an integer """
    # Display question and valid answers
    print(question)
    for i in range(len(choices)):
        print(str(i + 1) + ") " + choices[i])

    while True:
        try:  # Try convert user input to int
            choice = input("> ")
            if choice == "INVENTORY":
                display_inventory()
                print(question)
                continue

            choice = int(choice)
        except (TypeError, ValueError):  # Catch these exceptions (valid type)
            print("That is not a valid choice, must be an integer!")
        else:  # Else, they entered a integer
            # Check entered number is a valid number choice, else tell them it's not and restart loop
            if choice in [int(i + 1) for i in range(len(choices))]:
                return choice - 1
            else:
                print("That is not a valid choice!")


def display_inventory():
    print("-" * 50)
    if len(inventory):
        for item in inventory:
            print("-", item)
    else:
        print("You have no items in your inventory.")
    print("-" * 50)


def cell_1(first_time=False):
    global inventory

    print("-- CELL 1 --")
    if first_time:
        print("You awake in a dull unfamiliar room, not sure of how\n"
              "you came to be here. You observe the room around you\n"
              "are in and notice you are in a cell within a cell\n"
              "block. Your door isn't locked.\n")
        inventory = []
    else:
        print("You enter the cell you awoke in. You find nothing of\n"
              "use there.\n")

    choices = ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        cell_block()


def cell_2():
    print("-- CELL 2 --")
    print("You walk inside cell 2 and observe, you find nothing\n"
          "of interest.\n")

    choices = ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        cell_block()


def cell_3():
    print("-- CELL 3 --")
    print("You walk inside cell 3 and observe, you find nothing\n"
          "of interest.\n")

    choices = ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        cell_block()


def cell_4():
    print("-- CELL 4 --")
    print("You walk inside cell 4 and observe, you find nothing\n"
          "of interest.\n")

    choices = ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        cell_block()


def cell_block():
    print("-- CELL BLOCK --")
    print("You walk into the common space between the cells.\n"
          "You look around, the room is bare apart from the\n"
          "the four cells and a door in the corner.\n")

    choices = ["CELL 1", "CELL 2", "CELL 3", "CELL 4", "CORRIDOR"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "CELL 1":
        print("You head towards the door for cell 1...\n\n")
        cell_1()
    elif choices[answer] == "CELL 2":
        print("You head towards the door for cell 2...\n\n")
        cell_2()
    elif choices[answer] == "CELL 3":
        print("You head towards the door for cell 3...\n\n")
        cell_3()
    elif choices[answer] == "CELL 4":
        print("You head towards the door for cell 4...\n\n")
        cell_4()
    elif choices[answer] == "CORRIDOR":
        print("You head towards the door for the corridor...\n\n")
        corridor()


def cargo_bay_1():
    print("-- CARGO BAY 1 --")
    print("You walk inside cargo bay 1 and observe, you find\n"
          "nothing of interest.\n")

    choices = ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        corridor()


def cargo_bay_2():
    global inventory

    items = ["Ray Gun"]
    for item in items:
        for inventory_item in inventory:
            if inventory_item == item:
                print("ITEM REMOVE")
                items.remove(item)

    print("-- CARGO BAY 2 --")
    print("You walk inside cargo bay 2 and observe, you find\n"
          "nothing of interest.\n")

    choices = items + ["LEAVE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "Ray Gun":
        print("You walk towards the ray gun and pick it up.\n"
              "'Ray Gun' is now in your inventory.\n\n")

        inventory.append("Ray Gun")
        cargo_bay_2()
    if choices[answer] == "LEAVE":
        print("You head towards the door...\n\n")
        corridor()


def control_room():
    global inventory
    global name

    print("-- CONTROL ROOM --")
    print("You walk inside the control room and see the boss\n"
          "man in the corner.\n")

    if "Ray Gun" in inventory:
        choices = ["Shoot Boss"]
        answer = get_integer_input("SHOOT THE BOSS!", choices)

        if choices[answer] == "Shoot Boss":
            print("You take aim with you disgaured ray gun, aiming\n"
                  "towards the boss' head. You pull the trigger.\n"
                  "BOOM! The beast is dead.. bad ending, right?\n")
            win(name)
    else:
        print("You don't have any weapons. The boss turns and sees\n"
              "you. The door from which you entered is automatically\n"
              "locked. You cannot get out. The aliens lunges towards\n"
              "you. Blackness is the last thing you remember.")

        print("\n\nGame Over.")


def corridor():
    print("-- CORRIDOR --")
    print("You walk into a corridor between the main areas of\n"
          "place you awoke in. You look around and see 3 other\n"
          "doors which are labeled: Cargo Bay 1, Cargo Bay 2,\n"
          "and Control Centre.\n")

    choices = ["CELL BLOCK", "CARGO BAY 1", "CARGO BAY 2", "CONTROL CENTRE"]
    answer = get_integer_input("What do you do?", choices)

    if choices[answer] == "CELL BLOCK":
        print("You head towards the door for the cell block...\n\n")
        cell_block()
    elif choices[answer] == "CARGO BAY 1":
        print("You head towards the door for cargo bay 1...\n\n")
        cargo_bay_1()
    elif choices[answer] == "CARGO BAY 2":
        print("You head towards the door for cargo bay 2...\n\n")
        cargo_bay_2()
    elif choices[answer] == "CONTROL CENTRE":
        print("You head towards the door for the control room...\n\n")
        control_room()


def win(name):
    print("\n\n\n" + "-" * 100)
    print("You beaten the alien that has abducted you!")
    save_survivor(name)

    choices = ["Return to Menu"]
    answer = get_integer_input("Choose a menu option.", choices)

    if choices[answer] == "Return to Menu":
        menu()


def enter_name():
    global name
    name = get_string_input("What is your name?", "*")
    cell_1(True)


def save_survivor(name):
    file = open("survivors.txt", "a")
    file.write(name + "\n")
    file.close()


def view_survivors():
    file = open("survivors.txt", "r")
    survivors = file.readlines()
    file.close()

    for survivor in survivors:
        print(survivor)
    print("\n")

    choices = ["Return to Menu"]
    answer = get_integer_input("Choose a menu option.", choices)

    if choices[answer] == "Return to Menu":
        menu()


def menu():
    choices = ["Play", "View Survivors", "Quit"]
    answer = get_integer_input("Choose a menu option.", choices)

    if choices[answer] == "Play":
        enter_name()
    elif choices[answer] == "View Survivors":
        view_survivors()
    elif choices[answer] == "Quit":
        print("Thank you for playing.")
        quit()


menu()
