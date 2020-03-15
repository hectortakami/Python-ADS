
import collections
print("\n\n***************** BFS & DFS Q&A *****************\n")

# -------------------------------------------------------------------------
# PROBLEM 1: Determing wheter a BFS is valid or not
# INPUT: 
#       1.- VALID BST
#                           4
#                   2               5         => In-Order (LEFT -> PARENT -> RIGHT) 
#               1       3                        √ [ 1, 2, 3, 4, 5 ] (Ordered array)
# 
#       2.- NOT VALID BST
#                           3   
#                   2               4         => In-Order (LEFT -> PARENT -> RIGHT)           
#               1       5                        X [ 1, 2, 5, 3, 4 ] (Non-ordered array)
# 
# EXPLANATION: 
#               1) Do In-Order Traversal of the given tree 
#                  and store the result in a temp array.
#               2) Check if the temp array is sorted in ascending order, 
#                  if it is, then the tree is BST.
# -------------------------------------------------------------------------

class Node: 
	def __init__(self, value): 
		self.value = value 
		self.left_node = None
		self.right_node = None

def inorder_traversal(node, nodes_inorder):
    if node.left_node:
        inorder_traversal(node.left_node, nodes_inorder)
    nodes_inorder.append(node.value)
    if node.right_node:
        inorder_traversal(node.right_node, nodes_inorder)
    return nodes_inorder

def checkBST(root):
    tree_inorder = inorder_traversal(root, [])
    for i in range(0, len(tree_inorder) - 1):
        if tree_inorder[i] > tree_inorder[i + 1]:
            return 'NOT VALID BST :('
    return 'VALID BST :)'
        
def main():
    # First BST Tree
    root1 = Node(4)
    root1.left_node = Node(2)
    root1.left_node.left_node = Node(1)
    root1.left_node.right_node = Node(3)
    root1.right_node = Node(5)
    print('''

                [ TREE 1 ]

                    4
            2               5
        1       3

    ''')
    print(' In-Order: ' + str(inorder_traversal(root1, [])) + ' --> ' + checkBST(root1) + '\n\n')

    # Second BST Tree
    root2 = Node(3)
    root2.left_node = Node(2)
    root2.left_node.left_node = Node(1)
    root2.left_node.right_node = Node(5)
    root2.right_node = Node(4)
    print('''------------------------------------------------


                [ TREE 2 ]

                    3
            2               4
        1       5

    ''')
    print(' In-Order: ' + str(inorder_traversal(root2, [])) + ' --> ' + checkBST(root2) + '\n\n')


main()
print("\n***************** BFS & DFS Q&A *****************\n\n")
