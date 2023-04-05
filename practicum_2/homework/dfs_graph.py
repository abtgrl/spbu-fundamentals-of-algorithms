from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


# dfs_iterative
def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}
    stack = [node]

    while stack:
        n = stack.pop()

        if not visited[n]:
            visit(n)
            visited[n] = True

            for neighbor in G.neighbors(n):
                if not visited[neighbor]:
                    stack.append(neighbor)


def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}

    no_in_edges = []

    for node in G.nodes():
        if not visited[node]:
            if len(list(G.predecessors(node))) == 0:
                no_in_edges.append(node)

    while no_in_edges:
        node = no_in_edges.pop()
        visit(node)
        visited[node] = True
        successors = list(G.successors(node))
        G.remove_node(node)

        for successor in successors:
            if not visited[successor]:
                if len(list(G.predecessors(successor))) == 0:
                    no_in_edges.append(successor)


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("practicum_2/homework/graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "practicum_2/homework/graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
