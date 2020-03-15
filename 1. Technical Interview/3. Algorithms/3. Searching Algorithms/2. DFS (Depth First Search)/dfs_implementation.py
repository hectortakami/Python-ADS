print("\n\n\n***************** DEPTH FIRST SEARCH IMPLEMENTATION *****************\n")

'''
            9
    4               20
1       6       15      170

    DFS Traverses the tree by branches, until reach the bottom leafs

    Pre-Order   => [ 9, 4, 1, 6, 20, 15, 170 ]
    In-Order    => [ 1, 4, 6, 9, 15, 20, 170 ]
    Post-Order  => [ 1, 6, 4, 15, 170, 20, 9 ]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

class TreeDFS:
    def __init__(self):
        self.root = None
        self.num_nodes = 0
    
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

# ----------------------------------------------------------------------------------------------------
    def traverse_DFS_Preorder(self, node, data_list): # [  9, 4, 1, 6, 20, 15, 170 ]
        # Append the parent node 1st
        data_list.append(node.value)

        if node.left_node:
            # Append the left node 2nd
            self.traverse_DFS_Preorder(node.left_node, data_list)

        if node.right_node:
            # Append the right node 3rd
            self.traverse_DFS_Preorder(node.right_node, data_list)
        return data_list

# ----------------------------------------------------------------------------------------------------
    def traverse_DFS_Inorder(self, node, data_list): # [ 1, 4, 6, 15, 20, 170, 9 ]
        if node.left_node:
            # Append the left node 1st
            self.traverse_DFS_Inorder(node.left_node, data_list)

        # Append the parent node 2nd
        data_list.append(node.value)  

        if node.right_node:
            # Append the right node 3rd
            self.traverse_DFS_Inorder(node.right_node, data_list)
        return data_list
        
# ----------------------------------------------------------------------------------------------------
    def traverse_DFS_Postorder(self, node, data_list): #[ 1, 6, 4, 15, 170, 20, 9 ]
        if node.left_node:
            # Append the left node 1st
            self.traverse_DFS_Postorder(node.left_node, data_list)

        if node.right_node:
            # Append the right node 2nd
            self.traverse_DFS_Postorder(node.right_node, data_list)

        # Append the parent node 3rd
        data_list.append(node.value)
        return data_list


myDFS = TreeDFS()
myDFS.insert(9)
myDFS.insert(4)
myDFS.insert(6)
myDFS.insert(20)
myDFS.insert(15)
myDFS.insert(170)
myDFS.insert(1)

dfs_inorder = myDFS.traverse_DFS_Inorder(myDFS.root, [])
dfs_preorder = myDFS.traverse_DFS_Preorder(myDFS.root, [])
dfs_postorder = myDFS.traverse_DFS_Postorder(myDFS.root, [])

print('''
                9
            /       \\
        4               20
     /     \\         /      \\
    1       6       15      170
\n\n''')
print('\n    DFS Pre-Order  => ' + str(dfs_preorder) + '\n\t\t   ->( Parent -> LEFT -> RIGHT )')
print('\n\n    DFS In-Order   => ' + str(dfs_inorder) + '\n\t\t   ->( LEFT -> Parent -> RIGHT )')
print('\n\n    DFS Post-Order => ' + str(dfs_postorder) + '\n\t\t   ->( LEFT -> RIGHT -> Parent )\n\n')

# [ 9, 4, 1, 6, 20, 15, 170 ]

print("\n***************** DEPTH FIRST SEARCH IMPLEMENTATION *****************\n\n\n")
