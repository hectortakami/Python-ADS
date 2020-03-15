import collections
print("\n\n\n***************** BREADTH FIRST SEARCH IMPLEMENTATION *****************\n")

'''
            9
    4               20
1       6       15      170

    BFS Traverses the tree by levels, from left to right
    => [ 9, 4, 20, 1, 6, 15, 170 ]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

class TreeBFS:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self.root
        else:
            curr_node = self.root
            while True:
                if new_node.value < curr_node.value:
                    if curr_node.left_node == None:
                        curr_node.left_node = new_node
                        return
                    else:
                        curr_node = curr_node.left_node
                if new_node.value > curr_node.value:
                    if curr_node.right_node == None:
                        curr_node.right_node = new_node
                        return
                    else:
                        curr_node = curr_node.right_node

    def traverse_BFS(self):

        # Space Complexity O( n )
        # Keeps track of how the child nodes appear by each 
        # tree level, so then we can revisit them in order
        nodes_queue = collections.deque([])  # FIFO QUEUE (First In, First Out)

        # Output list with the node values sorted by level from left to right
        traversedBFS_list = []

        curr_node = self.root
        nodes_queue.append(curr_node)
        while len(nodes_queue) > 0:
            curr_node = nodes_queue.popleft()
            traversedBFS_list.append(curr_node.value)
            if curr_node.left_node != None:
                nodes_queue.append(curr_node.left_node)
            if curr_node.right_node != None:
                nodes_queue.append(curr_node.right_node)
        return traversedBFS_list

myBFS = TreeBFS()
myBFS.insert(9)
myBFS.insert(4)
myBFS.insert(6)
myBFS.insert(20)
myBFS.insert(15)
myBFS.insert(170)
myBFS.insert(1)

bfs_traversed = myBFS.traverse_BFS()
print('''
                9
            /       \\
        4               20
     /     \\         /      \\
    1       6       15      170
\n\n''')
print(' => ' + str(bfs_traversed) + '\n\n    BFS = ( By levels LEFT -> RIGHT )')



print("\n***************** BREADTH FIRST SEARCH IMPLEMENTATION *****************\n\n\n")

'''
            9
    4               20
1       6       15      170

    BFS Traverses the tree by levels, from left to right
    => [ 9, 4, 20, 1, 6, 15, 170 ]
'''