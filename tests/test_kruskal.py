import pytest
import logging
from minimum_spanning_tree.kruskal import kruskal

@pytest.fixture(autouse=True)
def print_test_name(request):
    logging.getLogger(__name__).info("Running test: %s", request.node.name)

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