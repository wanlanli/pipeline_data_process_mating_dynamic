import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def node_color(nodes, key: int = 0, p: int = 0, m: int = 0):
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
    node_colors = node_color(list(subgraph_directed.nodes), key, p, m)
    nx.draw(subgraph_directed, with_labels=True,
            pos=pos, font_weight='bold',
            node_color=node_colors, node_size=500, ax=ax)


def show_quantification(c_mating, data, id, time, ax=None):
    pairs = data[["p_id", "m_id"]].drop_duplicates()
    p, m = pairs.loc[id].astype(np.int_)
    print("pairs:", pairs.shape[0])
    ep_data = data.loc[id]
    p_dgree = ep_data.p_angle*180/np.pi
    m_dgree = ep_data.m_angle*180/np.pi

    p_coord = c_mating.cells[p].coordinates(time)[0]
    p_axis = p_coord[[0, 30]]
    p_contact = p_coord[ep_data.p_angle_index]

    m_coord = c_mating.cells[m].coordinates(time)[0]
    m_axis = m_coord[[0, 30]]
    m_contact = m_coord[ep_data.m_angle_index]

    p_s = c_mating.neighbor(p, frame=time, ctype=True)
    p_d = c_mating.neighbor(p, frame=time, ctype=False)

    m_s = c_mating.neighbor(m, frame=time, ctype=True)
    m_d = c_mating.neighbor(m, frame=time, ctype=False)

    ax.plot(p_axis[:, 1], p_axis[:, 0], "g")
    ax.plot(m_axis[:, 1], m_axis[:, 0], "r")

    ax.scatter(p_contact[1], p_contact[0], marker='o', c="g")
    ax.scatter(m_contact[1], m_contact[0], marker='o', c="r")

    for key in p_s:
        node_center = (c_mating.cells[key].center(frame=time)[0]).astype(np.float_)
        ax.scatter(node_center[1]+1, node_center[0]+1, marker="x", c='g')
        ax.text(node_center[1], node_center[0], key, c='g')

    for key in p_d:
        node_center = (c_mating.cells[key].center(frame=time)[0]).astype(np.float_)
        ax.scatter(node_center[1]+1, node_center[0]+1, marker="x", c='r')
        ax.text(node_center[1], node_center[0], key, c='r')

    for key in m_s:
        node_center = (c_mating.cells[key].center(frame=time)[0]).astype(np.float_)
        ax.scatter(node_center[1]-1, node_center[0]-1, marker="*", c='r')
        ax.text(node_center[1], node_center[0], key, c='r')

    for key in m_d:
        node_center = (c_mating.cells[key].center(frame=time)[0]).astype(np.float_)
        ax.scatter(node_center[1]-1, node_center[0]-1, marker="*", c='g')
        ax.text(node_center[1], node_center[0], key, c='g')
    print("angle p: ", p_dgree, ep_data.p_angle_index,
          "\nangle m: ", m_dgree, ep_data.m_angle_index)
