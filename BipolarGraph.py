from enum import Enum


class Node:
    

    
    def __init__(self, node_id: str, weight=0.0):        
        self.id = node_id 
        self.weight = weight        
        self.childs ={}
        self.paarent=self
        
    def set_weight(self, weight=0.0):
        self.weight = weight 
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.node_id == other.node_id
        else:
            return False
            
    def __hash__(self):
        return hash(self.id)            
        
    def __str__(self):
        return str(self.id) + " (" + str(self.weight) + ")"

class Edge:
    def __init__(self, src: Node, tgt: Node , weight=0.0):        
        self.src = src
        self.tgt = tgt        
        self.weight = weight         
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.src, self.tgt) == (other.src, self.tgt)
        else:
            return False

    def __hash__(self):
        return hash((self.src, self.tgt))
        
    def __str__(self):
        return str(self.id) + " " + str(self.weight)
        
class BipolarGraph:    
    
    def __init__(self):
        self.nodes = {}
        self.edges = {}    

    def add_node(self, node_id, weight=0.0):               
        if node_id not in self.nodes:
            node = Node(node_id, weight)
            self.nodes[node_id] = node
        else:
            node = self.nodes[node_id]
        
    def add_edge(self, src, tgt, weight: float = 0.0):
        edge = Edge(src, tgt, weight)
        self.edges[(src,tgt)] = edge
        self.nodes[tgt].childs[src]=self.nodes[src]
        self.nodes[src].parent=self.nodes[tgt]
        