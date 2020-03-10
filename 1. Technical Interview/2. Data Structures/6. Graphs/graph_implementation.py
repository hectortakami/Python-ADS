print("\n\n****************** GRAPH IMPLEMENTATION ******************\n")

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {
            # Stores the entire nodes connections 
            # EX. '0' : [ 1 , 2 ] -> the node with value 0 is conected with node 1 and node 2
        }
    
    def addVertex(self, node):
        if node in self.adjacent_list:
            print('Node already exists')
            return
        # Store a new dictionary using the node 
        # as key and the values as an empty array 
        # to keep the connections from that node to others
        self.adjacent_list[node] = []
        self.number_of_nodes += 1
        return node
        
    
    def addEdge(self, node1, node2):
    # Create the connection between 2 nodes UNDIRECTECTLY
        if node1 not in self.adjacent_list:
            print('Unexisting node ' + str(node1))
            return
        if node2 not in self.adjacent_list:
            print('Unexisting connection ' + str(node2) + ' for node ' + str(node1))
            return
        # The node2 is append to the connections of the node 1
        self.adjacent_list.get(node1).append(node2)
        return node2

    def showConnections(self):
        print('\nNodes in Graph: ( ' + str(self.number_of_nodes) + ' )\n')
        for key in self.adjacent_list:
            print('Node ' + str(key) + ': --> Connections: ' + str(self.adjacent_list.get(key)))

    
'''
    3   -   4   -   5
    |       |       |
    1   -   2       6
    \       /    
        0
'''
myGraph = Graph()

# All nodes in graph
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)

# Node 0 Connections
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 2)
# Node 1 Connections
myGraph.addEdge(1, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 0)
# Node 2 Connections
myGraph.addEdge(2, 4)
myGraph.addEdge(2, 1)
myGraph.addEdge(2, 0)
# Node 3 Connections
myGraph.addEdge(3, 1)
myGraph.addEdge(3, 4)
# Node 4 Connections
myGraph.addEdge(4, 3)
myGraph.addEdge(4, 2)
myGraph.addEdge(4, 5)
# Node 5 Connections
myGraph.addEdge(5, 4)
myGraph.addEdge(5, 6)
# Node 6 Connections
myGraph.addEdge(6, 5)

myGraph.showConnections()


print("\n\n****************** GRAPH IMPLEMENTATION ******************\n\n")