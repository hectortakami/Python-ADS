

print("\n\n\n*********** ARRAY IMPLEMENTATION *************\n")


class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return item

    def pop(self):
        lastItem = self.data[self.length - 1]
        self.data.pop(self.length - 1)
        self.length -= 1
        return lastItem

    def delete(self, index):
        deletedItem = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        self.pop()
        return deletedItem

    def printData(self):
        str = "[ "
        for i in range(0, self.length-1):
            str += self.data[i] + ", "
        str += self.data[self.length-1] + " ]"
        return str


myArray = MyArray()
myArray.push('one')
myArray.push('two')
myArray.push('three')

print("---------------------------------------\n\t" +
      myArray.printData() + "\n---------------------------------------")


print("\n POP() -> " + myArray.pop())
print(" =>" + myArray.printData() + "\n")

print("\n PUSH('four') -> " + myArray.push('four'))
print(" =>" + myArray.printData() + "\n")

print("\n DELETE(0) -> " + myArray.delete(0))
print(" =>" + myArray.printData() + "\n")


print("\n**********************************************\n\n\n")
