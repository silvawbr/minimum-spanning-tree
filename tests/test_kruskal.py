import pytest
import logging
from minimum_spanning_tree.kruskal import kruskal

@pytest.fixture(autouse=True)
def print_test_name(request):
    print(f"\nRunning test: {request.node.name}")

#empty network
empty_vertices = {}
empty_edges = []
empty_weights = {}

def test_kruskal_empty():
    assert kruskal((empty_vertices, empty_edges), empty_weights) == []

#one person network
one_person_vertices = {"A"}
one_person_edges = []
one_person_weights = {}

def test_kruskal_one_person():
    assert kruskal((one_person_vertices, one_person_edges), one_person_weights) == []

# two people network
two_people_vertices = {"A", "B"}
two_people_edges = [("A", "B")]
two_people_weights = {("A", "B"): 1.0}

def test_kruskal_two_people():
   assert kruskal((two_people_vertices, two_people_edges), two_people_weights) == [("A", "B")]

# three people network (no cycle)
three_people_vertices = {"A", "B", "C"}
three_people_edges = [("A", "B"), ("B", "C")]
three_people_weights = {("A", "B"): 1.0, ("B", "C"): 1.0}

def test_kruskal_three_people():
   assert kruskal((three_people_vertices, three_people_edges), three_people_weights) == [("A", "B"), ("B", "C")]

# simple cycle network
simple_cycle_vertices = {"A", "B", "C"}
simple_cycle_edges = [("A", "B"), ("B", "C"), ("C", "A")]
simple_cycle_weights = {("A", "B"): 1.0, ("B", "C"): 1.0, ("C", "A"): 1.0}

def test_kruskal_simple_cycle():
   assert kruskal((simple_cycle_vertices, simple_cycle_edges), simple_cycle_weights) == [("A", "B"), ("B", "C")]

# complex network
complex_vertices = {"A", "B", "C", "D", "E"}
complex_edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("C", "E"), ("A", "E")]
complex_weights = {("A", "B"): 1.0, ("A", "C"): 3.0, ("B", "C"): 2.0, ("B", "D"): 4.0, ("C", "D"): 1.0, ("D", "E"): 5.0, ("C", "E"): 2.0, ("A", "E"): 1.0}

def test_kruskal_complex():
    assert kruskal((complex_vertices, complex_edges), complex_weights) == [("A", "B"), ("C", "D"), ("A", "E"), ("B", "C")]