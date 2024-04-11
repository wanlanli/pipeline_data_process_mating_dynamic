import networkx as nx
import matplotlib.pyplot as plt


def node_color(nodes, key: int = 0, m: int = 0, p: int = 0):
    node_color = []
    for n in nodes:
        if n == key:
            c = "blue"
        elif n == m:
            c = "red"
        elif n == p:
            c = "green"
        else:
            c = "lightblue"
        node_color.append(c)
    return node_color


def draw_subgraph(g, key, p, m):
    f, ax = plt.subplots(figsize=(5, 5))
    undirected_g = g.to_undirected()
    nodes = nx.node_connected_component(undirected_g, key)
    subgraph = nx.subgraph(undirected_g, nodes)
    pos = nx.bfs_layout(subgraph, start=key)
    subgraph_directed = nx.subgraph(g, nodes)
    node_colors = node_color(nodes, key, p, m)
    nx.draw(subgraph_directed, with_labels=True,
            pos=pos, font_weight='bold',
            node_color=node_colors, node_size=500, ax=ax)
