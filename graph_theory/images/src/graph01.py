import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 3])
G.add_edges_from([(1, 2), (1, 3), (2, 3)])


G.nodes[1]['initial'] = 'A'
G.nodes[2]['initial'] = 'B'
G.nodes[3]['initial'] = 'C'
labels = nx.get_node_attributes(G, 'initial')
nx.draw(G, labels=labels, font_weight='bold')