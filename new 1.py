import random

room_loc_exits = {
    "backrow": ["up", "left", "right"],
    "backleft": ["up", "right"],
    "backright": ["up", "left"],
    "lowermiddle": ["up", "left", "down", "right"],
    "highermiddle": ["up", "left", "down", "right"],
    "rightside": ["up", "left", "down"],
    "leftside": ["up", "right", "down"],
    "toprow": ["right", "left", "down"],
    "topleft": ["right", "down"],
    "topright": ["left", "down"]
    }
    
room_loc = {
    "backrow": [1, 2, 3],
    "backleft": [0],
    "backright": [4],
    "lowermiddle": [6, 7, 8],
    "highermiddle": [11, 12, 13],
    "rightside": [9, 14],
    "leftside": [10, 5],
    "toprow": [16, 17, 18],
    "topright": [19],
    "topleft": [15]
    }

"""Empty room dict."""
room_dict = {}
for i in range(20):
    room_dict[i] = []

"""Picks one rooms with directions as to where the next room/s will be."""    
def random_rooms():
    rand = random.randint(0, 19)    
    next_room_no = {
        "up": rand + 5,
        "down": rand - 5,
        "left": rand - 1,
        "right": rand + 1
        }

    rand_room_dict = {}
    for rm_loc, loc_nums in room_loc.items():
        if rand in loc_nums:
            rand_room_dict[rand] = random.sample(room_loc_exits[rm_loc],
                random.randint(1, len(room_loc_exits[rm_loc])))
    for exits in rand_room_dict.values():
        temp_list = []
        for i in exits:
            i = (i, next_room_no[i])
            temp_list.append(i)
        rand_room_dict[rand] = temp_list
    next_room_list = []
    for test in rand_room_dict[rand]:
        dir, num = test
        next_room_list.append(num)
    return next_room_list
    

def random_rooms_test():
    rand_room_dict = {}    
    next_room_list = []   

    room_number = random.randint(0, 19)        
    next_room_no = {
        "up": room_number + 5,
        "down": room_number - 5,
        "left": room_number - 1,
        "right": room_number + 1
        }
    for length in range(20):
        if len(rand_room_dict) >= 1:
            for i in next_room_list:
                room_number = i
        else:
            
        for rm_loc, loc_nums in room_loc.items():
            if room_number in loc_nums:
                rand_room_dict[room_number] = random.sample(room_loc_exits[rm_loc],
                    random.randint(1, len(room_loc_exits[rm_loc])))
        for exits in rand_room_dict.values():
            temp_list = []
            for i in exits:
                i = (i, next_room_no[i])
                temp_list.append(i)
            room_dict[room_number] = temp_list
            rand_room_dict[room_number] = temp_list
        for test in rand_room_dict[room_number]:
            next_room_list.clear()
            dir, num = test
            next_room_list.append(num)
    return next_room_list
    
random_rooms_test()
print(room_dict)