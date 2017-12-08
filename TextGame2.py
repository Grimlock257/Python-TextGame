######################################################
# This version will load in scenes from JSON files
# This is not yet completed and does not function
# enough to actually play the game
######################################################

import json


def get_integer_input(question, choices):
    # Display question and valid answers
    print(question)
    for i in range(len(choices)):
        if isinstance(choices[i], Item):
            print(str(i + 1) + ") Pick up '" + choices[i].name + "'")
        else:
            print(str(i + 1) + ") " + choices[i])

    while True:
        choice = input("> ")
        if choice.lower() in ["inventory", "inv"]:
            player.inventory.view()
            print(question)
            continue

        try:  # Try convert user input to int
            choice = int(choice)
        except (TypeError, ValueError):  # Catch these exceptions (invalid type)
            print("That is not a valid choice, must be an integer!")
        else:  # Else, they entered a integer
            # Check entered number is a valid number choice, else tell them it's not and restart loop
            if choice in [int(i + 1) for i in range(len(choices))]:
                return choices[choice - 1], True if isinstance(choices[choice - 1], Item) else False
            else:
                print("That is not a valid choice!")


def get_string_input(question):
    print(question)
    while True:
        user_input = input("> ")

        confirm_input = input("Confirm you want to enter '" + user_input + "' for the question (Y/N):\n> ").lower()
        while confirm_input not in "yn":
            confirm_input = input("Enter Y or N:\n> ")

        if confirm_input == "y":
            return user_input
        else:
            print("You rejected your input. Enter new input:")


class Player:
    def __init__(self):
        self._inventory = Inventory()
        self._dead = False

    @property
    def inventory(self):
        return self._inventory

    def die(self):
        print("\n\n\nGame Over.")
        get_integer_input("", ["Menu"])
        self._dead = True
        menu()


class Item:
    def __init__(self, name, pick_up_text):
        self._name = name
        self._pick_up_text = pick_up_text.format(self._name)

    @property
    def name(self):
        return self._name

    @property
    def pick_up_text(self):
        return self._pick_up_text


class Inventory:
    def __init__(self, items=[]):
        self._inventory = items

    @property
    def inventory(self):
        return self._inventory

    def append(self, item):
        self._inventory.append(item)

    def remove(self, item):
        self._inventory.remove(item)

    def view(self):
        """ Output the inventory """
        print("-" * 50)
        if len(self._inventory):
            for i in range(len(self._inventory)):
                print("- ", self._inventory[i].name)
        else:
            print("You have no items in your inventory.")
        print("-" * 50)


class Scene:
    def __init__(self, name, first_entry_text, entry_text, choices, scene_inventory, required_items,
                 does_required_item_mean_death, death_text, lack_item_text):
        self._name = name
        self._first_entry_text = first_entry_text
        self._entry_text = entry_text
        self._choices = choices
        self._inventory = Inventory(scene_inventory)
        self._required_items = required_items
        self._does_required_item_mean_death = does_required_item_mean_death
        self._death_text = death_text
        self._lack_item_text = lack_item_text

        self._has_entered = False

    def enter(self):
        print("---", self._name, "---")
        print(
            self._first_entry_text if not self._has_entered and self._first_entry_text != "DEFAULT_FIRST_ENTRY_TEXT" else self._entry_text)

        self._has_entered = True

        if self._required_items:
            if all(item in player.inventory.inventory for item in self._required_items):
                print("|" * 100 + "You have the required items")
            else:
                if self._does_required_item_mean_death:
                    print(self._death_text)
                    player.die()
                else:
                    print(self._lack_item_text)

        # else:
        self.explore()

    def explore(self):
        answer_choice, is_item = get_integer_input("What do you do?", self._inventory.inventory + list(self._choices))
        if is_item:
            print(answer_choice.pick_up_text + answer_choice.name + "' is now in your inventory.\n\n")
            player.inventory.append(answer_choice)
            self._inventory.remove(answer_choice)
            self.explore()
        else:
            answer_result = self._choices.get(answer_choice)
            print(answer_result[0])
            globals()[answer_result[1]].enter()


def load_game(game):
    file = open(game + ".json")
    data = json.load(file)
    file.close()

    # Load items
    for item in data["items"]:
        item_data = data["items"][item]
        globals()[item] = Item(item_data["name"],
                               item_data.get("pick_up_text", "You walk towards '{}' and pick it up."))

    # Load scenes
    for scene in data["scenes"]:
        scene_data = data["scenes"][scene]

        # Assign inventory items to item objects
        for i, item in enumerate(scene_data.get("default_inventory", [])):
            scene_data["default_inventory"][i] = globals()[item]

        # Assign required items to item objects
        for i, item in enumerate(scene_data.get("required_items", [])):
            scene_data["required_items"][i] = globals()[item]

        # If there a key for this, then we set it to boolean True
        if scene_data.get("does_lack_required_mean_death", False):
            scene_data["does_lack_required_mean_death"] = True

        globals()[scene] = Scene(scene_data["name"],
                                 scene_data.get("first_entry_text", "DEFAULT_FIRST_ENTRY_TEXT"),
                                 scene_data["entry_text"],
                                 scene_data["choices"],
                                 scene_data.get("default_inventory", []),
                                 scene_data.get("required_items", []),
                                 scene_data.get("does_lack_required_mean_death", False),
                                 scene_data.get("death_text", "DEFAULT_DEATH_TEXT"),
                                 scene_data.get("lack_item_text", "DEFAULT_LACK_ITEM_TEXT"))


def create_game():
    def create_scene():
        print("Create Scene")
        name = get_string_input("Enter name of scene")
        entry_text = get_string_input("Enter the entry text for your scene")
        choices = []
        choices.append(get_string_input("You must have at least once choice for your room.\nEnter"))

    def create_item():
        print("Create Item")

    def save():
        print("Save")

    game_name = get_string_input("Enter the name of your game")

    choice, none = get_integer_input("Choose an option from the menu below:",
                                     ["Create new scene", "Create new item", "Save"])

    if choice == "Create new scene":
        create_scene()
    elif choice == "Create new item":
        create_item()
    elif choice == "Save":
        save()


def menu():
    print("Welcome.")

    choice, none = get_integer_input("Choose an option from the menu below:", ["Play", "Create Game", "Quit"])

    if choice == "Play":
        pass
    elif choice == "Create Game":
        pass
    elif choice == "Quit":
        quit()


# menu()
load_game("json_test")
player = Player()
cell_1.enter()
