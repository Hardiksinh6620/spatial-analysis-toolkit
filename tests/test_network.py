import pytest
from src.network import build_graph_from_edges,shortest_path,connected_components
def test_weighted_path():
    graph=build_graph_from_edges([(1,2,1),(2,3,1),(1,3,5)])
    assert shortest_path(graph,1,3)==[1,2,3]
def test_components_and_negative_weight():
    assert len(connected_components(build_graph_from_edges([(1,2,1),(3,4,1)])))==2
    with pytest.raises(ValueError): build_graph_from_edges([(1,2,-1)])
