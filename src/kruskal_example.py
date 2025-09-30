from minimum_spanning_tree.kruskal import kruskal

vertices = {"A", "B", "C", "D", "E"}

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
]

weights = {
    ("A", "B"): 1,
    ("A", "C"): 3,
    ("B", "C"): 2,
    ("B", "D"): 1,
    ("C", "D"): 1,
    ("C", "E"): 3,
    ("D", "E"): 2,
}

graph = (vertices, edges)

kruskal(graph, weights)