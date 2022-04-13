################################################
# LINKED LIST
################################################
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data;  # Assign data
        self.next = None;  # Initialize
                          # next as null
# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None;
    # Function to print nodes in a given linked list
    def printlist(self):
        curr_node = self.head
        while (curr_node):
            if curr_node.next is not None:
                print(curr_node.data, end=" -> ");
            else:
                print(curr_node.data, end="\n");
            curr_node = curr_node.next

# Big O = Upper Bound (Worst case)
# Big Omega (Q) = Lower Bound (Best case)
# Big Theta = Tight Bound (Best and Worst case are equal)

''' 
Amortized time: If an ArrayList gets out-of-space it doubles (2X) it size so the insertion won't take O(1)
                Although, this happens once in a while so it worths the extra time allocating space
                for special edge cases. 
                - TL;DR: Worst case happens every once in a while. But once it happens, it won't happen 
                         again for so long.
'''

# O(2^n) = Recursive
# O(log n) = Divide & Conquer
# O(N*M) = Nested loop (1st list length N and second M)
# O(N+M) = Two loops one executing after another
# O(N^2) = Iterating through the same size list in a nested manner

########################
# INTERVIEW QUESTIONS #
#######################

# ---------------------------------------------------------------------------------- #
''' removeDups(llist: LinkedList) -> Node
    v1 O(N) = Keeps iterating through the entire linked list to find if NEXT node has repeated data values, 
              if so we skip the next node and we link to the NEXT NEXT (x2 skip) until reach the end of the list.

Remove Dups: Write code to remove duplicates from an unsorted linked list.
'''        
def removeDups(llist: LinkedList):
    # Edge cases
    if llist.head is None or llist.head.next is None:
        return llist.head.data;

    seen_values = set();            # Creates a set() to store the values seen
    current = llist.head;           # Sets the 1st node to be the head
    seen_values.add(current.data);  # Store the head node value as the 1st seen data

    while current.next is not None:
        if current.next.data in seen_values:    # Validates if NEXT value is repeated
            current.next = current.next.next;   # If so, we skip the reference and jump to the next node
        else:
            seen_values.add(current.next.data); # If this value isn't seen we add it to the set
            current = current.next;             # We keep moving to the next reference ONLY (Not 2 as above). 
    return llist.head;
# ---------------------------------------------------------------------------------- #

''' returnElementFromLast(llist: LinkedList, n:int):
    v1 O(n) = Create a Deque to store in a reversed manner all node values, at the end just retrive the k'th element

Return k'th to Last: Implement an algorithm to find the kth to last element of a singly linked list.
'''
def returnElementFromLast(llist: LinkedList, k:int):
    current = llist.head;
    node_values = collections.deque();  # Create a deque to appendleft() and obtain a REVERSED list

    while current.next is not None:
        node_values.appendleft(current.data);   # Keep adding node.data when finding nodes
        current = current.next;
    node_values.appendleft(current.data);       # On the last node, also add it to the list
    
    if k <= len(node_values): 
        return node_values[k-1];    # Simply return the k'th element (k-1 because of the list indexes) if found
    else:   
        return -1;                  # Otherwise return "-1"
# ---------------------------------------------------------------------------------- #

''' deleteMiddleNode(llist: LinkedList)
    v1 O(n+[n/2]-1) or O(n) =
        1. Iterate through the entire list to get the length O(N)
        2. If length is EVEN find the middle index -2, if ODD find the middle index -1
        3. Iterate through the list the MIDLE_NUMBER times and change the pointers to skip the resulting middle node. 

Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
'''

def deleteMiddleNode(llist: LinkedList):
    llist_length = 1;       # Define length to be 1 (counting head)
    current = llist.head;   
    # Edge case, only 1 node list
    if current.next is None:
        return llist;

    while current.next is not None: 
        llist_length += 1;          # Iterate through list to get all length
        current = current.next;
    
    if llist_length % 2 == 0:
        middle_idx = (llist_length//2) - 2;     # If length is EVEN, get the middle -2
    else:
        middle_idx = (llist_length//2) - 1;      # If length is ODD, get the middle -1
        
    current_to_remove = llist.head;     # Create another temp pointer to iterate 
    for _ in range(0,middle_idx):       # only until reach the resulting middle index
        current_to_remove = current_to_remove.next;
    current_to_remove.next = current_to_remove.next.next;   # Once found, skip the reference to the middle node
    return llist;
# ---------------------------------------------------------------------------------- #
''' partition(llist: LinkedList, partitionPoint: int)
    v1 O(n) = Retrieve the list node values and sort them, thats all. 
              The partition point or order doesn't really matter.

Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
'''
def partition(llist: LinkedList, partitionPoint: int):
    node_values = collections.deque([]);
    current = llist.head;
    while current.next is not None:
        node_values.append(current.data);
        current = current.next;
    node_values = sorted(node_values);
    
    if partitionPoint not in node_values:
        return llist;
    else:
        # Recreate the linked list with the values sorted from node_values;
        return;
# ---------------------------------------------------------------------------------- #
''' sumLists(llist1: LinkedList, llist2: LinkedList) -> int
    v1 O(a+b) = Traverse linkedlist1 O(a) and linkedlist2 O(b) to obtain its values but stored them
                using Deque appendleft() to reverse them. Then convert them to string, cast it to 
                an integer and sum their results.

Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list. 
'''
def sumLists(llist1: LinkedList, llist2: LinkedList):
    llist1_values = collections.deque([])
    llist2_values = collections.deque([])
    current_ll1 = llist1.head;
    current_ll2 = llist2.head;

    while current_ll1.next is not None:
        llist1_values.appendleft(current_ll1.data);
        current_ll1 = current_ll1.next;
    llist1_values.appendleft(current_ll1.data);

    while current_ll2.next is not None:
        llist2_values.appendleft(current_ll2.data);
        current_ll2 = current_ll2.next;
    llist2_values.appendleft(current_ll2.data);

    num_ll1 = int(''.join(list(map(lambda x: str(x), llist1_values)))); # Reduce list to string and then to Int
    num_ll2 = int(''.join(list(map(lambda x: str(x), llist2_values)))); # Reduce list to string and then to Int
    
    print(str(num_ll1) + ' + ' + str(num_ll2) + ' = ' + str(num_ll1 + num_ll2) );
    return num_ll1 + num_ll2;
# ---------------------------------------------------------------------------------- #

''' palindrome(llist: LinkedList) -> bool
    v1 O(n) = Store linkedlist values in a list and then compare it with its reversed value.

Palindrome: Implement a function to check if a linked list is a palindrome. +
'''
def palindrome(llist: LinkedList):
    node_values = [];
    current = llist.head;
    while current.next is not None:
        node_values.append(current.data); 
        current = current.next;
    node_values.append(current.data); 
    return node_values == node_values[::-1];
# ---------------------------------------------------------------------------------- #

''' intersection(llist1: LinkedList, llist2) -> Node.data
    v1 O(m+n) = Iterate through both LinkedLists, save node values 
                in a list, get all matching values and return the 1st element.
                [Read assumption below].

Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. That is, if the k'th
node of the first linked list is the exact same node (by reference) as the j'th node of the second
linked list, then they are intersecting. 

NOTE: The v1 Implementation assumes we will 
      have the same linked nodes after findind the 
      1st intersected node and simply returns it. 
      If we need to validate the next nodes (starting from intersection)
      we need to add an additional loop to compare the sequence.
'''
def intersection(llist1: LinkedList, llist2):
    current_ll1 = llist1.head;
    current_ll2 = llist2.head;

    ll1_node_vals = [];
    ll2_node_vals = [];

    while current_ll1.next is not None: 
        ll1_node_vals.append(current_ll1.data);
        current_ll1 = current_ll1.next;
    ll1_node_vals.append(current_ll1.data);

    while current_ll2.next is not None: 
        ll2_node_vals.append(current_ll2.data);
        current_ll2 = current_ll2.next;
    ll2_node_vals.append(current_ll2.data);

    intersec_ll1_to_ll2 = [x for x in ll1_node_vals if x in ll2_node_vals];
    if len(intersec_ll1_to_ll2) > 0:
        return intersec_ll1_to_ll2[0];
    else:
        return 'No intersection';
# ---------------------------------------------------------------------------------- #
'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION: Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list. 
'''
def loopDetection(llist):
    node_vals = set();
    current = llist.head;
    while current.next is not None:
        if current.data in node_vals:
            return current.data;
        else:
            node_vals.add(current.data);
        current = current.next;
    if current.data in node_vals:
        return current.data;
    else:
        return 'No loop detected.'

# https://evalutron3001.googleplex.com/categoryquestions?category=Short%20Coding
# https://docs.python.org/3/library/collections.html
# file:///Users/htakami/Library/Containers/com.apple.BKAgentService/Data/Documents/iBooks/Books/CRACKING%20THE%20CODING%20INTERVIEW.pdf
def main():
    # loopDetection(llist)
    list1 = LinkedList()
    list1.head = Node('A')
    list1.head.next = Node('B')
    list1.head.next.next = Node('C')
    list1.head.next.next.next = Node('D')
    list1.head.next.next.next.next = Node('E')
    list1.head.next.next.next.next.next = Node('C')
    list1.printlist()       # INPUT: [ A -> B -> C -> D -> E -> C ]; 
    print(loopDetection(list1));   # RESULT: 'C'
    # ----------------------------------------------------------------- #
    '''
    # intersection(llist1: LinkedList, llist2)
    list1 = LinkedList()
    list1.head = Node('a1')
    list1.head.next = Node('a2')
    list1.head.next.next = Node('c1')
    list1.head.next.next.next = Node('c2')
    list1.head.next.next.next.next = Node('c3')
    list2 = LinkedList()
    list2.head = Node('b1')
    list2.head.next = Node('b2')
    list2.head.next.next = Node('b3')
    list2.head.next.next.next = Node('c1')
    list2.head.next.next.next.next = Node('c2')
    list2.head.next.next.next.next.next = Node('c3')
   
    list1.printlist();  # INPUT: [a1 -> a2 -> c1 -> c2 -> c3]
    list2.printlist();  # INPUT: [b1 -> b2 -> b3 -> c1 -> c2 -> c3]
    print(intersection(list1, list2));  # RESULT: 'c1' (node where intersects)
    
    list3 = LinkedList()
    list3.head = Node(2)
    list3.head.next = Node(6)
    list3.head.next.next = Node(4)
    list4 = LinkedList()
    list4.head = Node(1)
    list4.head.next = Node(5)
    
    list3.printlist();  # INPUT: [2 -> 6 -> 4]
    list4.printlist();  # INPUT: [1 -> 5]
    print(intersection(list3, list4));  # RESULT: 'No intersection'
    '''
    # ----------------------------------------------------------------- #
    '''
    # palindrome(llist: LinkedList)
    list1 = LinkedList()
    list1.head = Node('a')
    list1.head.next = Node('b')
    list1.head.next.next = Node('a')
    list1.printlist();
    print(palindrome(list1));

    list2 = LinkedList()
    list2.head = Node(1)
    list2.head.next = Node(2)
    list2.head.next.next = Node(3)
    list2.printlist();
    print(palindrome(list2));
    '''
    # ----------------------------------------------------------------- #
    '''
    # sumLists(llist1: LinkedList, llist2: LinkedList)
    list1 = LinkedList()
    list1.head = Node(7)
    list1.head.next = Node(1)
    list1.head.next.next = Node(6)

    list2 = LinkedList()
    list2.head = Node(5)
    list2.head.next = Node(9)
    list2.head.next.next = Node(2)
    
    list1.printlist();
    list2.printlist();
    sumLists(list1, list2);
    '''
    # ----------------------------------------------------------------- #
    '''
    # partition(llist: LinkedList, partitionPoint: int)
    list = LinkedList()
    list.head = Node(1)
    list.head.next = Node(4)
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(2)
    list.head.next.next.next.next = Node(5)
    list.head.next.next.next.next.next = Node(2)
    list.head.next.next.next.next.next.next = Node(3)
    list.printlist();                       # INPUT: [1 -> 4 -> 3 -> 2 -> 5 -> 2 -> 3] & (x = 3)
    partition(list, 3);
    list.printlist();                       # RESULT: [1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 5]
    '''
    # ----------------------------------------------------------------- #
    '''
    # deleteMiddleNode(llist: LinkedList):
    list = LinkedList()
    list.head = Node('a')
    list.head.next = Node('b')
    list.head.next.next = Node('c')
    list.head.next.next.next = Node('d')
    list.head.next.next.next.next = Node('e')
    list.head.next.next.next.next.next = Node('f')
    list.printlist();                       # INPUT: [a -> b -> c -> d -> e -> f]
    deleteMiddleNode(list);
    list.printlist();                       # RESULT: [a -> b -> d -> e -> f]
    '''
    # ----------------------------------------------------------------- #
    '''
    # returnElementFromLast(llist: LinkedList, n:int):
    list = LinkedList()
    list.head = Node(35)
    list.head.next = Node(15)
    list.head.next.next = Node(4)
    list.head.next.next.next = Node(20)
    list.printlist();                       # INPUT: [35 -> 15 -> 4 -> 20]
    print(returnElementFromLast(list, 2));  # RESULT: 4
    print(returnElementFromLast(list, 7));  # RESULT: -1
    '''
    # ----------------------------------------------------------------- #
    '''
    # removeDups(llist:LinkedList)
    list = LinkedList()
    list.head = Node(10)
    list.head.next = Node(12)
    list.head.next.next = Node(11)
    list.head.next.next.next = Node(11)
    list.head.next.next.next.next = Node(12)
    list.head.next.next.next.next.next = Node(11)
    list.head.next.next.next.next.next.next = Node(10)
    list.printlist();   # INPUT: [10 -> 12 -> 11 -> 11 -> 12 -> 11 -> 10]
    removeDups(list);       
    list.printlist();   # RESULT: [10 -> 12 -> 11]
    '''
    # ----------------------------------------------------------------- #
    return;
    
main();

