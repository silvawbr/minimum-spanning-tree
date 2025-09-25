from typing import Tuple, List, Set, Dict

Vertex = str
Edge = Tuple[Vertex, Vertex]
Graph = Tuple[Set[Vertex], List[Edge]]
WeightFunction = Dict[Edge, float]

def kruskal(g: Graph, w: WeightFunction) -> List[Edge]:
    A = []
    if not g[1]:
        return A
    if len(g[1]) <= 2:
        return g[1]
    raise NotImplementedError("Case not yet implemented.")