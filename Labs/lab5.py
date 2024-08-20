def breadth_first_search(network, initial_vertex):
    # Initialize a queue for the BFS process
    search_queue = [initial_vertex]
    # Set to keep track of visited vertices
    explored_vertices = set()
    # Mark the initial vertex as visited
    explored_vertices.add(initial_vertex)

    while search_queue:
        # Remove the front vertex from the queue
        active_vertex = search_queue.pop(0)
        print(active_vertex, end=' ')

        # Retrieve all adjacent vertices of the active vertex
        for adjacent_vertex in network[active_vertex]:
            if adjacent_vertex not in explored_vertices:
                # Add the adjacent vertex to the queue and mark it as visited
                search_queue.append(adjacent_vertex)
                explored_vertices.add(adjacent_vertex)

# Represent the graph as an adjacency list
network = {
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6', '7'],
    '3': ['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

# Execute BFS starting from vertex '0'
breadth_first_search(network, '0')

def bfs_with_target(network, initial_vertex, target_vertex):
    # Initialize a queue for the BFS process
    search_queue = [initial_vertex]
    # Set to keep track of visited vertices
    explored_vertices = set()
    # Mark the initial vertex as visited
    explored_vertices.add(initial_vertex)

    while search_queue:
        # Remove the front vertex from the queue
        active_vertex = search_queue.pop(0)
        print(active_vertex, end=' ')

        # If the target vertex is found, terminate the search
        if active_vertex == target_vertex:
            print("\nTarget vertex located:", active_vertex)
            return

        # Retrieve all adjacent vertices of the active vertex
        for adjacent_vertex in network[active_vertex]:
            if adjacent_vertex not in explored_vertices:
                # Add the adjacent vertex to the queue and mark it as visited
                search_queue.append(adjacent_vertex)
                explored_vertices.add(adjacent_vertex)

    print("\nTarget vertex not present in the graph.")

# Represent the graph with target as an adjacency list
network_with_target = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Execute BFS starting from vertex 'A' aiming for target vertex 'E'
bfs_with_target(network_with_target, 'A', 'E')


class MaxPriorityQueue:
    def __init__(self):
        self.entries = []

    def is_empty(self):
        return len(self.entries) == 0

    def insert(self, item, priority):
        self.entries.append((priority, item))

    def extract_max(self):
        if self.is_empty():
            return None
        
        # Identify the entry with the highest priority
        max_priority_index = 0
        for i in range(1, len(self.entries)):
            if self.entries[i][0] > self.entries[max_priority_index][0]:
                max_priority_index = i
        
        # Remove the entry with the highest priority
        max_priority_item = self.entries[max_priority_index][1]
        del self.entries[max_priority_index]
        return max_priority_item

    def peek_max(self):
        if self.is_empty():
            return None

        max_priority_index = 0
        for i in range(1, len(self.entries)):
            if self.entries[i][0] > self.entries[max_priority_index][0]:
                max_priority_index = i

        return self.entries[max_priority_index][1]

# Demonstration
priority_queue = MaxPriorityQueue()
priority_queue.insert("Task A", 2)
priority_queue.insert("Task B", 1)
priority_queue.insert("Task C", 3)

print("Entry with highest priority:", priority_queue.peek_max())  # Expected output: "Task C"

while not priority_queue.is_empty():
    print(priority_queue.extract_max(), end=' ')  # Expected order: "Task C Task A Task B"
