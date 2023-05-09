class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def print_solution(self, distances_from_source: list[int]) -> None:
        """
        Vertex 	 Distance from Source
        """
        print("Vertex \t Distance from Source")
        for vertex in range(self.vertices):
            print(vertex, "\t\t", distances_from_source[vertex])

    def minimum_distance(
        self, distances_from_source: list[int], visited: list[bool]
    ) -> int:
        """
        A utility function to find the vertex with minimum distance value, from the set
        of vertices not yet included in shortest path tree.
        """

        # Initialize minimum distance for next node
        minimum = 1e7
        min_index = 0

        # Search not nearest vertex not in the shortest path tree
        for vertex in range(self.vertices):
            if distances_from_source[vertex] < minimum and visited[vertex] is False:
                minimum = distances_from_source[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self, source: int) -> None:
        """
        Function that implements Dijkstra's single source shortest path algorithm for a
        graph represented using adjacency matrix representation.
        """

        distances = [int(1e7)] * self.vertices  # distances from the source
        distances[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.minimum_distance(distances, visited)
            visited[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and visited[v] is False
                    and distances[v] > distances[u] + self.graph[u][v]
                ):
                    distances[v] = distances[u] + self.graph[u][v]

        self.print_solution(distances)


graph = Graph(5)
graph.graph = [
    [
        0,
        7,
        9,
        0,
        0,
        14,
    ],
    [
        7,
        0,
        10,
        15,
        0,
        0,
    ],
    [
        9,
        10,
        0,
        11,
        0,
        2,
    ],
    [
        0,
        15,
        11,
        0,
        6,
        0,
    ],
    [
        0,
        0,
        0,
        6,
        0,
        9,
    ],
    [
        14,
        0,
        2,
        0,
        9,
        0,
    ],
]
graph.dijkstra(0)
