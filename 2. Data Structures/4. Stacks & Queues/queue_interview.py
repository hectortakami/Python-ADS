print("\n******************** QUEUES & STACKS | Q&A ********************\n\n")
# -------------------------------------------------------------------------
# PROBLEM 1: Implement a Queue (FIFO) using only Stacks (LIFO)
# -------------------------------------------------------------------------


class QueueStacked:
    def __init__(self):
        self.stack = []

    def peek(self):
        print('\n Peek: [ ' + str(self.stack[0]) + ' ] ')
        return self.stack[0]

    def enqueue(self, value):
        self.stack.append(value)
        print(' Enqueue(+) [ ' + str(value) + ' ] ')
        return value

    def dequeue(self):
        deleteValue = self.stack[0]
        self.stack.remove(deleteValue)
        print(' Dequeue(-) [ ' + str(deleteValue) + ' ] ')
        return deleteValue

    def prinQueueStacked(self):
        queueStackStr = '\n QueueStacked [ ' + str(len(self.stack)) + ' ]\n'
        queueStackStr += ' => [ '
        for i in range(0, len(self.stack)-1):
            queueStackStr += str(self.stack[i]) + ', '
        queueStackStr += str(self.stack[len(self.stack)-1]) + ' ]'
        print(queueStackStr)


def main():
    myQueueStacked = QueueStacked()
    myQueueStacked.enqueue('A')
    myQueueStacked.enqueue('B')
    myQueueStacked.enqueue('C')
    myQueueStacked.enqueue('D')
    myQueueStacked.enqueue('E')
    myQueueStacked.prinQueueStacked()
    myQueueStacked.peek()
    myQueueStacked.dequeue()
    myQueueStacked.prinQueueStacked()


main()
print("\n******************** QUEUES & STACKS | Q&A ********************\n\n")
