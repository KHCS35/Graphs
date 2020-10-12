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
    def __str__(self):
        return f"{self.stack}"


# def earliest_ancestor(ancestors, starting_node):
#     earliest_anc = None
#     #To find earliest ancestor, you have to find the earliest PATH
#     #creating an empty set to hold our paths
#     paths = []
#     #as you go through:
#     #create new paths
#     #each new path should have the previous node added to it
#     #Example: {[6], [6, 3], [6, 3, 1], [6, 3, 1, 10]}
#     #the last entry is the longest, so we'll grab the last number in that mini-list
#     def get_neighbors(current):
#         neighbor = []
#         for pair in ancestors:
#             if pair[-1] == current:
#                 neighbor.append(pair[0])
#                 # print(f"neighbor: {neighbor}")
#         return [neighbor]
#     #Creating a queue to start checking nodes
#     q = Queue()
#     q.enqueue([starting_node])
#     #creating a visited set to know which nodes we have or have not yet visited
#     visited = set()

#     #while the queue is not empty, we still have nodes to check.
#     while q.size() > 0:
#         # new_path = []
#         #getting our first node to check, saving it as v
#         v = q.dequeue()
#         latest_v = v[-1]
#         print(latest_v)

#         if latest_v not in visited:
#             visited.add(latest_v)

#             for n in get_neighbors(latest_v):
#                 neighbors = []
#                 neighbors.append(n)
#                 # print(neighbors)
#                 new_path = n
#                 print(new_path)
#                 q.enqueue(new_path)

#     return earliest_anc

def earliest_ancestor(ancestors, starting_node, path=None, paths=[], visited=None):
    # paths = []

    if path is None:
        path = [starting_node]
    else:
        path.append(starting_node)
    if visited is None:
        visited = set()
    # q = Queue()
    # q.enqueue(starting_node)
    # visited = set()
    
    def get_neighbors(current):
        neighbor = []
        for pair in ancestors:
            if pair[-1] == current:
                neighbor.append(pair[0])
                # print(f"neighbor: {neighbor}")
        return neighbor

    visited.add(starting_node)
    print(visited)

    if len(get_neighbors(starting_node)) == 0:
        paths.append(path)

    for neighbor in get_neighbors(starting_node):
        if neighbor not in visited:
            new_path = path + [neighbor]
            print(new_path)
            print(f"path: {path}")
        earliest_ancestor(ancestors, new_path[-1], path)
            
    # print("Final:")
    return paths
            

    

    
        

'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))

