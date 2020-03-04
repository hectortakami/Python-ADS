print("\n\n***************** LINKED LIST IMPLEMENTATION ******************\n")


class Node:
    def __init__(self, previousNode, nodeValue, nextNode):
        self.previousNode = previousNode
        self.nodeValue = nodeValue
        self.nextNode = nextNode

#  node1
#    3  --->  node2
#               7   --->  node3
#                           1  --->  node4
#                                      10   --->  node5
#                                                   16   ---> None


class LinkedList:
    def __init__(self, headValue):
        self.headNode = Node(None, headValue, None)
        self.tailNode = self.headNode
        self.length = 1

    def append(self, nodeValue):  # O(1)
        currentTail = self.tailNode
        newNode = Node(None, nodeValue, None)
        currentTail.nextNode = newNode
        newNode.previousNode = self.tailNode
        self.tailNode = newNode
        self.length += 1
        return newNode

    def prepend(self, nodeValue):  # O(1)
        currentHead = self.headNode
        newNode = Node(None, nodeValue, currentHead)
        currentHead.previousNode = newNode
        self.headNode = newNode
        self.length += 1
        return newNode

    def insert(self, position, value):  # O(n)
        if position >= self.length:
            print('Insertion index out of range')
            return self.append(value)
        nodeNum = 0
        currentNode = self.headNode
        while (nodeNum < position):
            currentNode = currentNode.nextNode
            nodeNum += 1

        newNode = Node(currentNode.previousNode, value, currentNode)
        currentNode.previousNode = newNode
        newNode.previousNode.nextNode = newNode
        self.length += 1
        return newNode

    def remove(self, position):  # O(n)
        if position >= self.length:
            print('Deletion index out of range')
            return None
        nodeNum = 0
        currentNode = self.headNode
        while (nodeNum < position):
            currentNode = currentNode.nextNode
            nodeNum += 1

        deleteValue = currentNode.nodeValue
        previousNode = currentNode.previousNode
        nextNode = currentNode.nextNode
        currentNode.previousNode.nextNode = nextNode
        currentNode.nextNode.previousNode = previousNode
        del currentNode
        self.length -= 1
        return deleteValue

    def printList(self):  # O(n)
        currentNode = self.headNode
        listStr = ' ' + str(currentNode.previousNode) + ' <= '
        while (currentNode.nextNode != None):
            listStr += '{ ' + str(currentNode.nodeValue) + ' } <=> '
            currentNode = currentNode.nextNode
        listStr += '{ ' + str(currentNode.nodeValue) + ' } => None'
        print(' Nodes: [ ' + str(self.length) + ' ]\n')
        print(listStr)

    def printListReversed(self):  # O(n)
        currentNode = self.tailNode
        listStr = ' ' + str(currentNode.nextNode) + ' <= '
        while (currentNode.previousNode != None):
            listStr += '{ ' + str(currentNode.nodeValue) + ' } <=> '
            currentNode = currentNode.previousNode
        listStr += '{ ' + str(currentNode.nodeValue) + ' } => None'
        print('\n\n Reversed | Nodes: [ ' + str(self.length) + ' ] \n')
        print(listStr)


myLinkedList = LinkedList('L')
myLinkedList.append('X')
myLinkedList.append(0)
myLinkedList.prepend('L')
myLinkedList.prepend('H')
myLinkedList.insert(1, 3)
myLinkedList.remove(4)
myLinkedList.printList()
myLinkedList.printListReversed()

print("\n***************************************************************\n")
