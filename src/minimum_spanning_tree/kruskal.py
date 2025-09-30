from typing import Tuple, List, Set, Dict

# Premissas:
# sendo Edge = (u, v) => u e v estão ordenados alfabeticamente
# w contém o peso de todas as arestas do grafo g

Vertex = str
Edge = Tuple[Vertex, Vertex]
Graph = Tuple[Set[Vertex], List[Edge]]
WeightFunction = Dict[Edge, float]

def find_set(vertex_set: Dict[Vertex, Vertex], v: Vertex) -> Vertex:
    if vertex_set[v] == v:
        return vertex_set[v]
    return find_set(vertex_set, vertex_set[v])

def kruskal(g: Graph, w: WeightFunction) -> List[Edge]:
    A = []
    if not g[1]:
        return A
    vertex_set = {v: v for v in g[0]}
    rank = {v: 0 for v in g[0]}
    sorted_edges = sorted(g[1], key=lambda edge: w[edge])
    for edge in sorted_edges:
        u, v = edge
        rootU = find_set(vertex_set, u)
        rootV = find_set(vertex_set, v)
        if rootU != rootV:
            if rank[rootU] < rank[rootV]:
                vertex_set[rootU] = rootV
            elif rank[rootU] > rank[rootV]:
                vertex_set[rootV] = rootU
            else:
                vertex_set[rootV] = rootU
                rank[rootU] += 1
            A.append(edge)
            if len(A) == len(g[0]) - 1:
                break
    print(f"Grafo base da investigação - Esqueleto da rede criminosa: {A}")
    return A
