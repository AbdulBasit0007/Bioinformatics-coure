from node import Node
from network import Network


class FileNetwork(Network):
    """
    Creates a network from a network file, where each row consists of two columns, denoting two nodes that
    are connected by an edge.
    """
    def __init__(self, file_path: str, delimiter='\t', undirected=True, allow_self_edges=False):
        """
        Specification:
        - Skip rows with no, one, or more than 2 columns.
        - Do not produce errors when adding data to the network (e.g. adding an edge more than once).
        - It is fine if the network file is empty, the result is just an empty network.
        - If an unhandled error occurs while opening the file (e.g. the file does not exist), that is okay.

        :param file_path: path to the network file
        :param delimiter: symbol between columns in a row, default is a tab
        :param undirected: True if the network has undirected edges, False if the network is directed (optional)
        :param allow_self_edges: True if nodes are allowed to have edges to themselves, False otherwise (optional)
        """
        # Initialize the Network superclass
        super().__init__(undirected=undirected, allow_self_edges=allow_self_edges)

        # Open the network file and read its contents according to the parameters
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # Split the line into two columns
                    columns = line.strip().split(delimiter)
                    if len(columns) == 2:
                        node1, node2 = columns
                        # Convert node identifiers to integers
                        node1 = int(node1)
                        node2 = int(node2)
                        # Add nodes and edges to the network
                        self.add_node(node1)
                        self.add_node(node2)
                        self.add_edge(node1, node2)
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Returning an empty network.")
        except Exception as e:
            print(f"An error occurred while reading the network file: {e}. Returning an empty network.")
