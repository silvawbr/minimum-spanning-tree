from typing import Tuple, List, Set, Dict

# Premissas:
# sendo Edge = (u, v) => u e v estão ordenados alfabeticamente
# w contém o peso de todas as arestas do grafo g

Vertex = str
Edge = Tuple[Vertex, Vertex]
Graph = Tuple[Set[Vertex], List[Edge]]
WeightFunction = Dict[Edge, float]

def find_set(vertex_set: Dict[Vertex, Tuple[Vertex, int]], v: Vertex) -> Tuple[Vertex, int]:
    if vertex_set[v][0] == v:
        return vertex_set[v]
    return find_set(vertex_set, vertex_set[v][0])

def kruskal(g: Graph, w: WeightFunction) -> List[Edge]:
    A = []
    if not g[1]:
        return A
    vertex_set = {v: (v, 0) for v in g[0]}
    sorted_edges = sorted(g[1], key=lambda edge: w[edge])
    for edge in sorted_edges:
        u, v = edge
        parentU, rankU = find_set(vertex_set, u)
        parentV, rankV = find_set(vertex_set, v)
        if parentU != parentV:
            if rankU < rankV:
                vertex_set[parentU] = (parentV, rankU)
            elif rankU > rankV:
                vertex_set[parentV] = (parentU, rankV)
            else:
                vertex_set[parentV] = (parentU, rankV)
                vertex_set[parentU] = (parentU, rankU + 1)
            A.append(edge)
            if len(A) == len(g[0]) - 1:
                break
    print(f"Grafo base da investigação - Esqueleto da rede criminosa: {A}")
    return A