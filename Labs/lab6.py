# ---------4.1 Solution

# Class to represent a graph and perform DFS traversal
class GraphTraversal:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, start_vertex, end_vertex):
        self.adjacency_list[start_vertex].append(end_vertex)

    def dfs_helper(self, current_vertex, visited_vertices):
        visited_vertices[current_vertex] = True
        print(current_vertex, end=' ')

        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if not visited_vertices[adjacent_vertex]:
                self.dfs_helper(adjacent_vertex, visited_vertices)
    
    def perform_dfs(self, start_vertex):
        visited_vertices = [False] * self.num_vertices
        self.dfs_helper(start_vertex, visited_vertices)


# Main block to create a graph and perform DFS traversal
if __name__ == "__main__":
    graph = GraphTraversal(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Depth First Traversal starting from vertex 2:")
    graph.perform_dfs(2)


# ---------6.1 Solution

# GraphTraversal class using string labels with goal detection
class StringGraphTraversal:
    def __init__(self):
        self.adjacency_list = {}
        self.goal_found = False  # To track if the goal vertex is found

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.adjacency_list:
            self.adjacency_list[start_vertex] = []
        self.adjacency_list[start_vertex].append(end_vertex)

    def dfs_helper(self, current_vertex, visited_vertices):
        if self.goal_found:
            return  # Exit if the goal has been located

        visited_vertices.add(current_vertex)
        print(current_vertex, end=' ')
        
        if current_vertex == 'G':  # Check if current vertex is the goal
            print("Goal vertex 'G' found")
            self.goal_found = True  # Mark the goal as found
            return  # Terminate DFS

        for adjacent_vertex in self.adjacency_list.get(current_vertex, []):
            if adjacent_vertex not in visited_vertices:
                self.dfs_helper(adjacent_vertex, visited_vertices)
    
    def perform_dfs(self, start_vertex):
        visited_vertices = set()
        self.dfs_helper(start_vertex, visited_vertices)


# Main block to create a graph with string labels and perform DFS traversal
if __name__ == "__main__":
    graph = StringGraphTraversal()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'F')
    graph.add_edge('A', 'D')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'K')
    graph.add_edge('B', 'J')
    graph.add_edge('D', 'G')
    graph.add_edge('E', 'C')
    graph.add_edge('E', 'H')
    graph.add_edge('E', 'I')
    graph.add_edge('I', 'L')
    graph.add_edge('K', 'N')
    graph.add_edge('K', 'M')

    print("Depth First Traversal starting from vertex 'A':")
    graph.perform_dfs('A')
