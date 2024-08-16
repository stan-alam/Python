import igraph as ig
from igraph import Graph
g_colleagues=ig.Graph(
 edges=[(0,1),(0,2),(1,2)],n=3,directed=False)
ig.plot(g_colleagues,bbox= (200,200), vertex_size=40,
 vertex_label=["A","B","C"])