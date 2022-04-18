from collections import deque
from logging import root
import math
import queue
################################################
# BINARY TREE NODE
################################################
class Node:
    def __init__(self, data):
        self.data = data;  # Node data or value
        self.left = None;  # Left of Node
        self.right = None;  # Right of Node

    ############# BREADTH FIRST SEARCH TRAVERSALS #############
    def levelOrderTraversal(self,root):
        queue = deque([]);
        current = root;
        while current is not None:
            print(current.data, end=' ');
            if current.left is not None:
                queue.append(current.left);
            if current.right is not None:
                queue.append(current.right);
            if bool(queue):
                current = queue.popleft();   
            else:
                break;             
        return;

    ############## DEPTH FIRST SEARCH TRAVERSALS ##############
    # NODE, LEFT, RIGHT
    def preOrderTraversal(self, node):     
        if not node:
            return;
        print(node.data, end=' ');
        node.preOrderTraversal(node.left);
        node.preOrderTraversal(node.right);
    # LEFT, NODE, RIGHT
    def inOrderTraversal(self, node):     
        if not node:
            return;
        node.inOrderTraversal(node.left);
        print(node.data, end=' ');
        node.inOrderTraversal(node.right);
    # LEFT, RIGHT, NODE
    def postOrderTraversal(self, node):     
        if not node:
            return;
        node.preOrderTraversal(node.left);
        node.preOrderTraversal(node.right);
        print(node.data, end=' ');

########################
# INTERVIEW QUESTIONS #
#######################

# Note: A Tree is a Graph, the main difference is that most of the trees have a ROOT Node with 2 or more childs.

# Binary Tree: Every Node has 2 and ONLY 2 child nodes.
# Binary Search Tree (BST): All left child nodes are SMALLER than the ROOT Node (including their childs) and the same on 
#                     the right, they must be GREATER than the ROOT node in question.
# Tree size (2^k -1)= k is the horizontal number of levels

# (BFS) Breadth First Search = Uses a queue rather than recursive algorithms
# (DFS) Depth First Search = Recursively iterates the node childs and then the node (depneding the traversal order choosed)

# CLARIFICATIONS NEEDED FOR INTERVIEW PROBLEMS
# 1. Is the tree balanced or unbalanced? (all levels filled in order, left to right)
# 2. If BST, does it need to follow the strict 
#    implementation (all smaller children must be on left and greater on right)?
# 3. Do not assume a binary tree is perfect.

# ========================================================================================
# ===================================== TREES ============================================
# ========================================================================================
''' minimalTree(arr: list) -> BST
    v1 0(n/2) + O(1) = O(n); We are splitting the tree in halfs (n/2) and then getting the middle point
                             of the working SUBLIST (1). 

Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an 
algorithm to create a binary search tree with minimal height. 
'''
def minimalTree(arr: list):
    if not arr:     # IMPORTANT! Recursion ending condition
        return None;
    middle_index = len(arr)//2;     # Find the middle point of 
    root = Node(arr[middle_index]); # the list (the ROOT Node)

    root.left = minimalTree(arr[:middle_index]);    # Recursively assign the LEFT SUBLIST
                                                    # to be the LEFT NODE of the root

    root.right = minimalTree(arr[middle_index+1:]); # Recursively assign the RIGHT SUBLIST
                                                    # to be the RIGHT NODE of the root
    return root; # IMPORTANT! Recursion ending condition
# ----------------------------------------------------------------------------------------- #
''' binaryToLevelLists(root: Node)
    v1 O(2n) : We 1st iterate ulevel by level using BFS and then by calculating log2(N) and 2^N
               we obtain the total amount of levels in the tree and the maximum amount of nodes to allocate 
               per level.

Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

ASUMPTION: This code implementation is intended to BALANCED trees only, making sure we 
are filling every level before adding another one.
'''

def binaryToLevelLists(root: Node):
    queue = deque([]);
    current = root;
    nodes = [];
    # BFS to get all nodes ordered level by level
    while current is not None:
        nodes.append(current.data);
        if current.left is not None:
            queue.append(current.left);
        if current.right is not None:
            queue.append(current.right);
        if bool(queue):
            current = queue.popleft();   
        else:
            break;
    # The amount of nodes LOG BASE 2 will return the TREE HEIGHT (LEVELS)
    levels = math.ceil(math.log2(len(nodes)))

    start = 0;
    level_number = 1;
    for x in range(0,levels):
        max_nodes_in_level = int(math.pow(2,x));   # 1, 2, 4, 8, 16, 32 ...
        end = start+max_nodes_in_level
        sub = nodes[start:end];
        # HERE WE CAN SEND THE LIST TO BE MODIFIED AS LINKED LIST
        print('L' + str(level_number) + ': ' + str(sub));
        start = end;
        level_number+=1;
    return;
# ----------------------------------------------------------------------------------------- #

''' checkBalanced(root) -> bool
    v1 O(n): Recursively verify the height between sides of the tree O(n) because action 
             will repeat for every node in the tree. If the difference between the right and the left side
             is not greater than 1 we can say its balanced. Otherwise it is not.

Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

NOTE: For this problem, a height-balanced binary tree is defined as:
      a binary tree in which the left and right subtrees of every node 
      differ in height by no more than 1.
'''
# function to find height of binary tree
def height(root):
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def checkBalanced(root):
    # Base condition, if tree is empty its considered as balanced
    if root is None:
        return True
    # Get the height from the left side and the right side of the tree
    left_height = height(root.left)
    right_height = height(root.right)
    # Check if right & left subtrees are balanced
    is_left_subtree_balanced = checkBalanced(root.left); 
    is_right_subtree_balanced = checkBalanced(root.right); 

    # If the height difference (between left & right) is LESS THAN 1 level
    # and the subtrees of each side are balanced we can conclude the entire tree is balanced
    if abs(left_height-right_height) <= 1:
        return is_left_subtree_balanced and is_right_subtree_balanced;
    # Otherwise the tree is NOT balanced.
    else:
        return False
# ----------------------------------------------------------------------------------------- #

''' validateBST(root) -> bool
    v1 O(n): This approach seems correct but its WRONG it will not identify the greater elements on the left subtrees.
    v2 O(n): The main difference with the previous implementation is that we add a reference point
             (the previous node) to compare against their childrens. We need to add the reference with
             the "min" and "max" values seen when using recursion. (for root we define the arbitrary max an min).

Validate BST: Implement a function to check if a binary tree is a binary search tree. 

Note: A BST does not have duplicate values and all LESS values in the left side are smaller
than the node (the same on right where all values must be GREATER).
'''

def validateBSTv2(root:Node, prev_min=-10000, prev_max=10000):
    # Base condition to stop the recursion on leaf nodes
    if root is None:
        return True;
    # If the RIGHT value is SMALLER to the previous node is NOT a BST
    if root.data < prev_min:
        return False;
    # If the LEFT value is GREATER to the previous node is NOT a BST
    if root.data > prev_max:
        return False;

    is_left_BST = validateBSTv2(root.left, prev_min, root.data);    # Recursively compare LEFT side with the MAX value
    is_right_BST = validateBSTv2(root.right, root.data, prev_max);  # Recursively compare RIGHT side with the MIN value

    return is_left_BST and is_right_BST;



def validateBSTv1(root):
    # Base condition to stop recursion
    if root is None:
        return True;
    current = root;
    if current.left is not None:
        if current.left.data > current.data :
            return False;
    if current.right is not None:
        if current.right.data < current.data :
            return False;
    if validateBSTv1(current.left) is False or validateBSTv1(current.right) is False:
        return False;
    return True;
# ----------------------------------------------------------------------------------------- #

''' inOrderSuccesor(root: Node, succ:int) -> int
    v1 O(h): We traverse the tree 'in-order' to get the sorted sequence of nodes, then we step in
             the node of our interest and retreive the NEXT GREATEST node value.

Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent. 
'''

def _inorderTraversal(root: Node, queue=deque([])):
    if not root:
        return;
    if root.left is not None:
        _inorderTraversal(root.left, queue);
    queue.append(root.data);
    if root.right is not None:
        _inorderTraversal(root.right, queue);
    return queue;

def inOrderSuccesor(root: Node, succ:int):
    # Traverse inOrder the tree and store it as a queue
    in_order_queue = _inorderTraversal(root);
    # Find the index where the node of interest is at
    idx_node_to_succeed = list(in_order_queue).index(succ);
    # If its on the list iterate from its position+1 onwards to 
    # find the NEXT HIGHEST NODE in comparision with it.
    if idx_node_to_succeed < len(in_order_queue)-1:
        for next_idx in range(idx_node_to_succeed+1, len(in_order_queue)):
            if in_order_queue[next_idx] > in_order_queue[idx_node_to_succeed]:
                return in_order_queue[next_idx];
    return -1;
# ----------------------------------------------------------------------------------------- #
'''
    v1 O(log2) divide & conquer search = Evaluate the values we are searching n1 & n2, 
         if BOTH are SMALLER move to the left side of the tree, if BOTH are GREATER move to 
         the right subtree, but if they create a RANGE with the CURRENT NODE (that means 
         one is smaller and the other greater) you can consider it as the LOWEST COMMON ANCESTOR.

First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
'''

def firstCommonAncestor(root: Node, n1, n2):
    if root is None:
        return;
    # If BOTH search values are SMALLER than the current node
    # we move our search to the lef subtree
    if n1 < root.data and n2 < root.data :
        return firstCommonAncestor(root.left, n1, n2);
    # If BOTH search values are GREATER than the current node
    # we move our search to the right subtree 
    if n1 > root.data and n2 > root.data:
        return firstCommonAncestor(root.right, n1, n2);
    # If we see a discrepancy where one value can be SMALLER and the other GREATER
    # than the current node, we can definetely say we reach a common ancestor and return it.
    return root;


def main():
    ###################### TREES ######################
    ''' # firstCommonAncestor(root, n1, n2);
    root = Node(20);
    root.left = Node(8);
    root.right = Node(22);
    root.left.left = Node(4);
    root.left.right = Node(12);
    root.left.right.left = Node(10);
    root.left.right.right = Node(14);
                                    #              20  
                                    #        08           22
                                    #    04     12           
                                    #         10  14

    commonAncestor1 = firstCommonAncestor(root, 10, 14);
    print(commonAncestor1.data);    # RESULT: 12 (between '10' & '14' only '12' is the first parent)
    commonAncestor1 = firstCommonAncestor(root, 4, 14);
    print(commonAncestor1.data);    # RESULT: 8 (between '4' & '14' only '8' is the first parent)
    commonAncestor1 = firstCommonAncestor(root, 10, 22);
    print(commonAncestor1.data);    # RESULT: 20 (between '10' & '22' only '22' is the first parent)
    '''
    #-------------------------------------------------#
    ''' # inOrderSuccesor(root: Node, succ:int)
    root = Node(20);
    root.left = Node(8);
    root.right = Node(22);
    root.left.left = Node(4);
    root.left.right = Node(12);
    root.left.right.left = Node(10);
    root.left.right.right = Node(14);
                                    #              20  
                                    #        08           22
                                    #    04     12           
                                    #         10  14
                                    # In-Order Traversal: [4, 8, 10, 12, 14, 20, 22]

    print(inOrderSuccesor(root, 8));    # Result: 10
    print(inOrderSuccesor(root, 10));   # Result: 12
    print(inOrderSuccesor(root, 14));   # Result: 20
    '''
    #-------------------------------------------------#
    ''' # validateBST(root) -> bool
    root1 = Node(8);
    root1.left = Node(4);
    root1.right = Node(10);
    root1.left.left = Node(2);
    root1.left.right = Node(6);
    root1.right.right = Node(20);
                                    #              08  
                                    #        04           10
                                    #    02     06            20

    print(validateBSTv2(root1));    # RESULT: True 
                                    # All elements on left/right are smaller/grater than parent nodes
    root2 = Node(8);
    root2.left = Node(4);
    root2.right = Node(10);
    root2.left.left = Node(2);
    root2.left.right = Node(12);
    root2.right.right = Node(20);
                                    #              08  
                                    #        04           10
                                    #    02     12            20

    print(validateBSTv2(root2));    # RESULT: False 
                                    # Node '12' is on LEFT side of root node '8'
    '''
    #-------------------------------------------------#
    ''' # checkBalanced(root)
    root1 = Node('A');
    root1.left = Node('B');
    root1.right = Node('C');
    root1.left.left = Node('D')
                                    #  L1→            A  
                                    #  L2→      B           C*
                                    #  L3→  *D

    print(checkBalanced(root1));       # RESULT: True 
                                    # is balanced because only 1 level differs 
                                    # between left subtree and right subtree (Left=L3, Right=L2)

    root2 = Node('A')
    root2.left = Node('B')
    root2.right = Node('C')
    root2.left.left = Node('D')
    root2.left.right = Node('E')
    root2.left.left.left = Node('F')
                                    #  L1→             A  
                                    #  L2→       B           C*
                                    #  L3→    D     E
                                    #  L4→ *F

    print(checkBalanced(root2));       # RESULT: False 
                                    # is NOT balanced because 2 level differ on height 
                                    # between left subtree and right subtree (Left=L4, Right=L2)
    '''
    #-------------------------------------------------#
    ''' # binaryToLevelLists(root: Node)
    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    root.right.left = Node(6);
    root.right.right = Node(7);
    root.left.left.left = Node(8);
    root.left.left.right = Node(9);
                                    #  L1→            1  
                                    #  L2→      2           3
                                    #  L3→  4       5   6       7 
    binaryToLevelLists(root);
                                    #  L1→ [1]
                                    #  L2→ [2, 3]
                                    #  L3→ [4, 5, 6, 7]
    '''
    #-------------------------------------------------#
    ''' # DEPTH FIRST SEARCH (NODE & LEFT/RIGHT SIDES SEQUENCED)
        # minimalTree()
    root = minimalTree([1, 2, 3, 4, 5, 6, 7]);
                                    #              4  
                                    #        2           6
                                    #    1       3   5       7
    print( '\nIn-Order: ' ); 
    root.inOrderTraversal(root);    # RESULT: 1 2 3 4 5 6 7 [LEFT,NODE,RIGHT]
    print( '\nPre-Order: ' );
    root.preOrderTraversal(root);   # RESULT: 4 2 1 3 6 5 7 [NODE,LEFT,RIGHT]
    print( '\nPost-Order: ' );
    root.postOrderTraversal(root);  # RESULT: 2 1 3 6 5 7 4 [LEFT,RIGHT,NODE]
    print('\n');
    '''
    #-------------------------------------------------#
    ''' # BREADTH FIRST SEARCH (LEVEL ORDERED)
    root = Node('A');
    root.left = Node('B');
    root.right = Node('C');
    root.left.left = Node('D');
    root.left.right = Node('E');
    root.left.right.left = Node('F');
                                    #  L1→            A  
                                    #  L2→      B           C
                                    #  L3→  D       E          
                                    #  L4→        F
                                    
    root.levelOrderTraversal(root); # RESULT: [A ,B ,C ,D, E, F]
    '''
    
main();