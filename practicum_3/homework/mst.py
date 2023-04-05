from typing import Any

from queue import PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    mst_set.add(start_node)
    rest_set.remove(start_node)

    q = PriorityQueue()

    for neighbor in G.neighbors(start_node):
        edge = (start_node, neighbor)
        q.put((G.edges[edge]["weight"], edge))

    while len(rest_set):
        weight, edge = q.get()
        new_node = edge[1]

        if new_node not in mst_set:
            mst_edges.add(edge)
            mst_set.add(new_node)
            rest_set.remove(new_node)
        else:
            continue

        for neighbor in G.neighbors(new_node):
            edge = (new_node, neighbor)
            q.put((G.edges[edge]["weight"], edge))

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
