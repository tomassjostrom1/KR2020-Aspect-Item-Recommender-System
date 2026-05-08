import networkx as nx
from BipolarGraph import BipolarGraph

def draw_graph(graph: BipolarGraph):
    G = nx.Graph()
    G.add_node(1)
    nx.draw(G)