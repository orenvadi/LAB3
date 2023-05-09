import networkx as nx

nodes = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2),
    (1, 3),
    (1, 6),
    (2, 3),
    (3, 4),
    (6, 3),
    (6, 5),
    (2, 4),
    (4, 5),
]
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
incidence_matrix = -nx.incidence_matrix(G, oriented=True)
# ^ this returns a scipy sparse matrix, can convert into the full array as below
# (as long as your node count is reasonable: this'll have that squared elements)
print(incidence_matrix.toarray())
