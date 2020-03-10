print("\n\n****************** BINARY SEARCH TREE IMPLEMENTATION ******************\n")


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):  # O( log n )
        new_node = Node(data)
        if not self.root:
            # If root not existing we assign it
            self.root = new_node
            return

        current_node = self.root
        while True:
            if data < current_node.data:
                # Left Insertion (Minor Values)
                if current_node.left == None:
                    current_node.left = new_node
                    return
                else:
                    # Keep going through left until find a 'None' leave
                    current_node = current_node.left

            elif data > current_node.data:
                # Right Insertion (Mayor Values)
                if current_node.right == None:
                    current_node.right = new_node
                    return
                else:
                    # Keep going through right until find a 'None' leave
                    current_node = current_node.right

    def lookup(self, search_value):  # O( log n )
        if not self.root:
            return None
        current_node = self.root
        while True:
            if current_node == None:
                return False
            if current_node.data == search_value:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def remove(self, search_value):  # O( log n )
        if not self.root:
            return False

        current_node = self.root
        parent_node = None  # We have to keep track of the previous node
        while (current_node):
            if search_value < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif search_value < current_node.data:
                parent_node = current_node
                current_node = current_node.right
            elif search_value == current_node.data:
                # We reach the node that matches
                # Option 1: The node doesn't have right child
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        if current_node.data < parent_node.data:
                            # If parent > current value, make current left child a child of parent
                            parent_node.left = current_node.left
                        elif current_node.data > parent_node.data:
                            # If parent < current value, make left child a rigth child of parent
                            parent_node.right = current_node.left

                elif current_node.right.left == None:
                    # Option 2: Rigth child without (No) left child
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left
                        if current_node.data < parent_node.data:
                            # If parent > current value, make right child of the left the parent
                            parent_node.left = current_node.right
                        elif current_node.data > parent_node.data:
                            # If parent < current value, make right child a rigth child of parent
                            parent_node.right = current_node.right
                else:
                    # Option 3: Rigth child with left child
                    # Find the Right child's left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left != None:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node == None:
                        self.root = left_most
                    else:
                        if current_node.data < parent_node.data:
                            parent_node.left = left_most
                        elif current_node.data > parent_node.data:
                            parent_node.right = left_most
            return True


def printTreeFormatted(node, level=0):
    if (node):
        nodeStr = ''
        if (level == 0):
            nodeStr += ('*') + '\n'
        if (level < 2):
            nodeStr += (('  ' * level) + '| ') + '\n'
            nodeStr += (('  ' * level) + '+- ' + str(node.data))
            print(nodeStr)
        if (level >= 2):
            nodeStr += (('  |' * (level-1)) + '  | ') + '\n'
            nodeStr += (('  |' * (level-1)) + '  +- ' + str(node.data))
            print(nodeStr)

    if (node.left or node.right):
        nextLevel = level + 1
        if (node.left):
            printTreeFormatted(node.left, nextLevel)
        if (node.right):
            printTreeFormatted(node.right, nextLevel)


myBSTree = BinarySearchTree()
myBSTree.insert(9)
myBSTree.insert(4)
myBSTree.insert(6)
myBSTree.insert(20)
myBSTree.insert(15)
myBSTree.insert(170)
myBSTree.insert(1)

x = myBSTree.lookup(6)
print('\n Lookup [ 6 ] : ' + str(x))
y = myBSTree.lookup(9)
print(' Lookup [ 9 ] : ' + str(y) + '\n')

printTreeFormatted(myBSTree.root)
'''
            9
    4               20
1       6       15      170       
'''


print('\n-------------------------------------\n')

myBSTree.remove(9)

x = myBSTree.lookup(9)
print('\n Lookup [ 9 ] : ' + str(x) + '\n')
printTreeFormatted(myBSTree.root)

'''
            15
    4               20
1       6               170       
'''


print("\n\n***********************************************************************\n")
