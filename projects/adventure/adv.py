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
reverse_path = []

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
[]Create a function that can tell if the current room has any unexplored
areas
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

def has_unexplored(room_id):
    current = map[room_id]
    #output for room 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    for direction in current:
        if current[direction] == '?':
            return direction
    # print(current)

reverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


# initialize_room(0)
# print(map)
# has_unexplored(0)
#Result: {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}

# Create a breadth first search that checks the rooms in my graph for
# any unexplored locals.

# print(len(room_graph))

def dft():
    #unexplored rooms
    unexplored_rooms = []


    q = Stack()
    q.push(player.current_room.id)
    visited = set()

    while q.size() > 0:

        v = q.pop()
        # print(v)

        #if we haven't yet visited it
        if v not in visited:
            visited.add(v)
            initialize_room(v)
            # print(map)
        #if our exits have any unexplored paths
        num_of_unex = 0
        for d in map[v]:
            if map[v][d] == '?':
                # print(f"count of default value: {map[v][d].count('?')}")
                unexplored_rooms.append(d)
            print(f"thingy: {map[v][d]}")
            num_of_unex += map[v][d].count('?')
            # print(num_of_unex)
        
        #if this triggers then we've already explored the exits here
        if num_of_unex == 0:
            player.travel(reverse_path[-1])
            q.push(player.current_room.id)
            num_of_unex = 0
        #else, we still have rooms to explore:
        else:
            random.shuffle(unexplored_rooms)
            rand_direction = unexplored_rooms[0]
            print(f"Random direction: {rand_direction}")
            player.travel(rand_direction)
            map[v][rand_direction] = player.current_room.id
            traversal_path.append(rand_direction)
            reverse_path.append(reverse_directions[rand_direction])
            # print(f"reverse path: {reverse_path}")
            unexplored_rooms = []
            print(map)
            q.push(player.current_room.id)
        
        if len(traversal_path) == len(room_graph):
            return
        
        # print(unexplored_rooms)

                

# print(map)
dft()

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
