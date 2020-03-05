print("\n\n***************** STACKS IMPLEMENTATION ******************\n")


class Stack:
    def __init__(self):
        self.array = []

    def peek(self):  # O(1)
        if (len(self.array) <= 0):
            return None
        print('\n Peek : [ ' + str(self.array[len(self.array)-1]) + ' ]')
        return self.array[len(self.array)-1]

    def push(self, value):  # O(1)
        self.array.append(value)
        print(' Push(+) [ ' + str(value) + ' ]')
        return self.array[len(self.array)-1]

    def pop(self):  # O(1)
        if (len(self.array) <= 0):
            return None
        deleteValue = self.array[len(self.array)-1]
        self.array.pop()
        print(' Pop(-) [ ' + str(deleteValue) + ' ]')
        return deleteValue

    def printStack(self):  # O(n)
        stackStr = ' => [ '
        for i in range(len(self.array)-1, 0, -1):
            stackStr += str(self.array[i]) + ', '
        stackStr += str(self.array[0]) + ' ] '
        print(' \n Items [ ' + str(len(self.array)) + ' ]\n')
        print(stackStr)
        return


myStack = Stack()
myStack.push('W')
myStack.push('O')
myStack.push('L')
myStack.push('F')
myStack.push('R')
myStack.push('E')
myStack.push('V')
myStack.push('O')
myStack.printStack()

myStack.peek()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.printStack()
myStack.peek()


print("  \n********************** STACK ARRAY ***********************\n\n")
