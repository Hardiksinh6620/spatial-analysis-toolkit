"""Weighted network helpers."""
import networkx as nx
def build_graph_from_edges(edges):
    graph=nx.Graph()
    for source,target,weight in edges:
        if weight<0: raise ValueError("weights must be non-negative")
        graph.add_edge(source,target,weight=weight)
    return graph
def shortest_path(graph,source,target): return nx.shortest_path(graph,source,target,weight="weight")
def connected_components(graph): return list(nx.connected_components(graph))
