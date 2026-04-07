class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)

    def __bool__(self):
        return len(self.data) > 0

def bfs_search(starting_vertex, search_value):
    queue = Queue()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    while queue:
        current_vertex = queue.dequeue()

        if current_vertex.value == search_value:
            return current_vertex

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
                queue.enqueue(adjacent_vertex)

    return None

v1 = Vertex("alice")
v2 = Vertex("bob")
v3 = Vertex("candy")
v4 = Vertex("derek")
v5 = Vertex("elaine")
v6 = Vertex("fred")
v7 = Vertex("gina")
v8 = Vertex("helen")
v9 = Vertex("irena")

v1.add_adjacent_vertex(v2)
v1.add_adjacent_vertex(v3)
v1.add_adjacent_vertex(v4)
v1.add_adjacent_vertex(v5)
v2.add_adjacent_vertex(v6)
v6.add_adjacent_vertex(v8)
v8.add_adjacent_vertex(v3)
v4.add_adjacent_vertex(v5)
v4.add_adjacent_vertex(v7)
v4.add_adjacent_vertex(v9)

print(f"Search for 'bob': {bfs_search(v1, 'bob')}")
print(f"Search for 'zebra': {bfs_search(v1, 'zebra')}")
print(f"Search for 'helen': {bfs_search(v1, 'helen')}")
print("---------------------------------------------------")
print(f"Search for 'bob': {bfs_search(v5, 'bob')}")
print(f"Search for 'zebra': {bfs_search(v5, 'zebra')}")
print(f"Search for 'helen': {bfs_search(v5, 'helen')}")