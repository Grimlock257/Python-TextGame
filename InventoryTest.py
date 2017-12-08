import json
from pprint import pprint

game = {
    "scenes": {
        "cell_1": {"name": "CELL 1",
                   "entry_text": "You enter the cell you awoke in. You find nothing of use there. ",
                   "choices": {"LEAVE": ["You head towards the door...", "cell_block"]},
                   "default_inventory": [],
                   "required_items": []},

        "cell_2": {"name": "CELL 2",
                   "entry_text": "You enter the cell you awoke in. You find nothing of use there. ",
                   "choices": {"LEAVE": ["You head towards the door...", "cell_block"]},
                   "default_inventory": [],
                   "required_items": []},

        "cell_3": {"name": "CELL 3",
                   "entry_text": "You enter the cell you awoke in. You find nothing of use there. ",
                   "choices": {"LEAVE": ["You head towards the door...", "cell_block"]},
                   "default_inventory": [],
                   "required_items": []},

        "cell_4": {"name": "CELL 4",
                   "entry_text": "You enter the cell you awoke in. You find nothing of use there. ",
                   "choices": {"LEAVE": ["You head towards the door...", "cell_block"]},
                   "default_inventory": [],
                   "required_items": []},

        "cell_block": {"name": "CELL BLOCK",
                       "entry_text": "You walk into the common space between the cells. You look around, the room is bare apart from the the four cells and a door in the corner. ",
                       "choices": {"CELL 1": ["You head towards the door for cell 1...", "cell_1"],
                                   "CELL 2": ["You head towards the door for cell 2...", "cell_2"],
                                   "CELL_3": ["You head towards the door for cell 3...", "cell_3"],
                                   "CELL_4": ["You head towards the door for cell 1...", "cell_4"],
                                   "CORRIDOR": ["You head towards the door for the corridor...", "corridor"]},
                       "default_inventory": [],
                       "required_items": []},

        "cargo_bay_1": {"name": "CARGO BAY 1",
                        "entry_text": "You walk inside cargo bay 1 and observe, you find nothing of interest. ",
                        "choices": {"LEAVE": ["You head towards the door...", "corridor"]},
                        "default_inventory": [],
                        "required_items": []},

        "cargo_bay_2": {"name": "CARGO BAY 2",
                        "entry_text": "You walk inside cargo bay 2 and observe, you find nothing of interest. ",
                        "choices": {"LEAVE": ["You head towards the door...", "corridor"]},
                        "default_inventory": ["ray_gun"],
                        "required_items": []},

        "control_room": {"name": "CONTROL ROOM",
                         "entry_text": "You walk inside the control room and see the boss man in the corner. ",
                         "choices": {"LEAVE": ["You head towards the door...", "corridor"]},
                         "default_inventory": [],
                         "required_items": ["ray_gun"]},

        "corridor": {"name": "CORRIDOR",
                     "entry_text": "You walk into a corridor between the main areas of place you awoke in. You look around and see 3 other doors which are labeled: Cargo Bay 1, Cargo Bay 2, and Control Centre. ",
                     "choices": {"CELL BLOCK": ["You head towards the door for the cell block...", "cell_block"],
                                 "CARGO BAY 1": ["You head towards the door for cargo bay 1...", "cargo_bay_1"],
                                 "CARGO BAY 2": ["You head towards the door for cargo bay 2...", "cargo_bay_2"],
                                 "CONTROL ROOM": ["You head towards the door for the control room...",
                                                  "control_room"]},
                     "default_inventory": [],
                     "required_items": []}
    },
    "items": {
        "digaurded_ray_gun": {"name": "Ray Gun"}
    }
}

file = open("json_test.json", "w")
data = json.dump(game, file, indent=4)
file.close()

file = open("json_test.json")
data = json.load(file)
file.close()

pprint(data)
