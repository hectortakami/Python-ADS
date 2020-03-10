print("\n\n***************** QUEUE IMPLEMENTATION ******************\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first
        self.length = 0

    def peek(self):  # O(1)
        if (self.length <= 0):
            return None
        print('\n Peek : [ ' + str(self.first.value) + ' ]')
        return self.first.value

    def enqueue(self, value):  # O(1)
        newItem = Node(value)
        if self.length <= 0:
            self.first = newItem
            self.last = newItem
        else:
            self.last.nextNode = newItem
            self.last = newItem
        self.length += 1
        print(' Enqueue(+) [ ' + str(newItem.value) + ' ]')
        return newItem

    def dequeue(self):  # O(1)
        deleteValue = self.first.value
        removeFirst = self.first
        self.first = self.first.nextNode
        removeFirst.nextNode = None
        del removeFirst
        self.length -= 1
        print(' Dequeue(-) [ ' + str(deleteValue) + ' ]')
        return deleteValue

    def printQueue(self):  # O(n)
        currentItem = self.first
        queueStr = ' => [ '
        while (currentItem.nextNode != None):
            queueStr += (str(currentItem.value) + ', ')
            currentItem = currentItem.nextNode
        queueStr += str(currentItem.value) + ' ]\n'
        print(' \n Queueing [ ' + str(self.length) + ' ]\n')
        print(queueStr)
        return


myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')
myQueue.enqueue('Q')
myQueue.enqueue('U')
myQueue.printQueue()

myQueue.peek()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.printQueue()

myQueue.enqueue(3)
myQueue.enqueue('U')
myQueue.enqueue(3)
myQueue.printQueue()

myQueue.peek()
myQueue.dequeue()
myQueue.printQueue()


print("\n******************* QUEUE LINKED LIST *******************\n\n")
