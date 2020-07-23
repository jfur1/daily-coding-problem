# You are given a list of data entries that represent entries and exits of groups of people into a building. 
# An entry looks like this:

# {"timestamp": 1526579928, count: 3, "type": "enter"}

# This means 3 people entered the building. An exit looks like this:

# {"timestamp": 1526580382, count: 2, "type": "exit"}

# This means that 2 people exited the building. timestamp is in Unix time.

# Find the busiest period in the building, that is, the time with the most people in the building. 
# Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, 
# i.e. with 0 people inside.

def busiestPeriod(data):
    # Keep track of current # of people in the building, as well as the max. #
    maxPeople = 0
    nPeople = 0
    start = end = 0
    # Flag for when we need to mark the end timestamp for max people
    updateEnd = False

    for entry in data.values():
        
        # Add People
        if(entry["type"] == "enter"):
            nPeople += entry["count"]
            # Check if this is the most people there have been
            if nPeople > maxPeople: 
                maxPeople = nPeople
                start = entry["timestamp"]
                # Next time people exit, we will have to store this as the end of our maximum group of people
                updateEnd = True

        # Remove People
        elif(entry["type"] == "exit"):
            nPeople -= entry["count"]
            # updateEnd 
            if updateEnd:
                end = entry["timestamp"]
                updateEnd = False   
    
    return [(start, end), maxPeople]


data = { 0: {"timestamp": 1526579928, "count": 3, "type": "enter"}, 
        1:  {"timestamp": 1526580382, "count": 2, "type": "exit"}, 
        2:  {"timestamp": 1526580482, "count": 4, "type": "enter"}, 
        3: {"timestamp": 1526580582, "count": 3, "type": "exit"},
        4: {"timestamp": 1526580682, "count": 4, "type": "enter"},
        5:{"timestamp": 1526580782, "count": 3, "type": "exit"},
        6:{"timestamp": 1526580882, "count": 5, "type": "enter"},
        7:{"timestamp": 1526580982, "count": 3, "type": "exit"},
        8:{"timestamp": 1526581482, "count": 1, "type": "enter"},
        9:{"timestamp": 1526582482, "count": 6, "type": "exit"} }

res = busiestPeriod(data)
print('Maximum Number of People in the Building:', res[1])
print("Started at:", res[0][0])
print("Ended at:", res[0][1])