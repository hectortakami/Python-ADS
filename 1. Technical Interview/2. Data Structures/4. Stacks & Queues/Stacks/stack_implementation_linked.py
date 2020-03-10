print("\n\n***************** STACKS IMPLEMENTATION ******************\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):  # O(1)
        if (self.length <= 0):
            return None
        print('\n Peek : [ ' + str(self.top.value) + ' ]')
        return self.top.value

    def push(self, value):  # O(1)
        newItem = Node(value)
        newItem.nextNode = self.top
        self.top = newItem
        self.length += 1
        print(' Push(+) [ ' + str(self.top.value) + ' ]')
        return newItem

    def pop(self):  # O(1)
        if (self.length <= 0):
            return None
        removeTop = self.top
        deleteValue = self.top.value
        self.top = removeTop.nextNode
        removeTop.nextNode = None
        self.length -= 1
        print(' Pop(-) [ ' + str(deleteValue) + ' ]')
        del removeTop
        return deleteValue

    def printStack(self):  # O(n)
        currentItem = self.top
        stackStr = ' => [ '
        while (currentItem.nextNode != None):
            stackStr += str(currentItem.value) + ', '
            currentItem = currentItem.nextNode
        stackStr += str(currentItem.value) + ' ] '
        print(' \n Items [ ' + str(self.length) + ' ]\n')
        print(stackStr)
        return


myStack = Stack()
myStack.push('Amazon')
myStack.push('Google')
myStack.push('Outlook')
myStack.push('Facebook')
myStack.printStack()

myStack.peek()
myStack.pop()
myStack.printStack()

myStack.peek()
myStack.pop()
myStack.printStack()


print("\n******************* STACK LINKED LIST ********************\n\n")
