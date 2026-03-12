import random
from network import Network
from node import Node

class ScaleFreeNetwork(Network):
    """
    This network class implements a scale-free, undirected network without self-edges.
    """
    def __init__(self, n_nodes=0, n_edges_per_iteration=0):
        if n_nodes < 0:
            raise ValueError("Number of nodes cannot be negative.")
        if n_edges_per_iteration < 0:
            raise ValueError("Number of edges per iteration cannot be negative.")
        
        # Initialize the Network superclass
        Network.__init__(self, undirected=True, allow_self_edges=False)
        
        # Add initial nodes
        for i in range(n_nodes):
            # Create a new Node object with identifier i
            node = Node(identifier=i)
            # Add the new Node object to the network
            self.add_node(node)
        
        # Barabási–Albert algorithm
        for i in range(n_nodes):
            # Create a new node with a unique identifier
            new_node = Node(identifier=i + n_nodes)
            # Add the new node to the network
            self.add_node(new_node)
            
            # Compute probabilities only once
            prob_connect = self.compute_probabilities(new_node)
            
            # Establish edges from the new node to randomly selected existing nodes
            if i < n_edges_per_iteration:
                m_edges = i + 1
            else:
                m_edges = n_edges_per_iteration
            
            connected_count = 0
            while connected_count < m_edges:
                existing_node = random.choices(list(prob_connect.keys()), weights=prob_connect.values(), k=1)[0]
                if existing_node != new_node and not self.edge_exists(new_node, existing_node):
                    self.add_edge(new_node, existing_node)
                    connected_count += 1
    
    def compute_probabilities(self, new_node):
        degree_sum = sum(node.degree() for node in self.nodes.values() if node != new_node)
        
        # Check if degree_sum is zero
        if degree_sum == 0:
            # Handle the case when sum of degrees is zero
            # For example, you can return a default probability distribution
            return {node: 1 / len(self.nodes) for node in self.nodes.values() if node != new_node}
        
        # Compute probabilities and return
        return {node: node.degree() / degree_sum for node in self.nodes.values() if node != new_node}
