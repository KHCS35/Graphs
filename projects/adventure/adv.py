from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
What is being asked:
Construct a traversal graph.
I'll start in room 0, and it will contain a list of possible exits
My stating graph should look like this:
    {
        0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    }
    Those placeholder '?' values will allow me to determine which
    room have been explored
If I move south from room 0, my graph should add a new entry
and some data can be added:
    {
        0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
        5: {'n': 0, 's': '?', 'w': '?', 'e': '?'}
    }
    Since we went south, we found room 5, we need to initialize that room
    and start putting in data we know of. Such as that south of room 0
    is room 5, and similarly, north of room 5 is room 0.

My work is complete with my graph has a number of entries equal to 
the number of rooms. My algorithm should log the path with each time I 
invoke the player.travel() function.

Each move I make should not be random, it has to be decided by looking at 
the surrounding rooms and finding out which ones have unexplored areas.

My Game-Plan:
[X]Create an empty graph
[X]Create a function that takes the current room id, and it's possible exits
and adds them to a graph in the right format.
[]Create a breadth first search that checks the rooms in my graph for
any unexplored locals.
'''
#Creating an empty graph
map = {}

#Create a function that takes the current room id, and it's possible exits
#and adds them to a graph in the right format.

print(f"Starting Room: {player.current_room.id}")

def initialize_room(room_id):
    #room_id will come from player.current_room.id
    possible_directions = player.current_room.get_exits()
    exits_obj = {}
    for direction in possible_directions:
        #setting each possible direction in the room to the default value
        exits_obj[direction] = '?'
    map[room_id] = exits_obj

# initialize_room(0)
# print(map)
#Result: {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
    





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
