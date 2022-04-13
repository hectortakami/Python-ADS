from collections import deque
from math import ceil, floor

# Big O = Upper Bound (Worst case)
# Big Omega (Q) = Lower Bound (Best case)
# Big Theta = Tight Bound (Best and Worst case are equal)

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

# STAK = LIFO
# QUEUE = FIFO

########################
# INTERVIEW QUESTIONS #
#######################
# ---------------------------------------------------------------------------------- #
''' StackMin Class
    v1 O(n) = Use the min() Python in-built function
    v2 O(1) = Keep track of the last minimum number seen and ther return it.

Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum eiement? Push, pop and min should ail operate in 0(1) time.
'''
class StackMin:
    def __init__(self):
        self.arr = deque();
        self.min_seen = None;   # Empty integer

    def pop(self):
        return self.arr.popleft();

    def push(self, value):
        if self.min_seen is None:
            self.min_seen = value;
        if self.min_seen is not None and value < self.min_seen:
            self.min_seen = value;
        return self.arr.appendleft(value);

    def min(self):
        # OPTION 1: Use min() Python in-built function
        # return min(self.arr);
        # OPTION 2: When pushing, keep track of the smallest number seen
        return self.min_seen;

    def display(self):
        print(list(self.arr));
# ---------------------------------------------------------------------------------- #

'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStack s that mimics this. SetOfStack s should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStack s .push() and SetOfStack s .pop() should behave identically to a single stack
(that is, pop( ) should return the same values as it would if there were just a single stack). 
'''
class SetOfStack:
    def __init__(self, capacity_per_stack:int):
        self.stack_list = deque();
        self.stacks = 0;
        self.capacity = capacity_per_stack;
    def push(self, value):
        # HANDLE EMPTY LIST OF STACKS
        if not bool(self.stack_list):           
            self.stack_list.append(deque([]));
            self.stacks = 1;
        # HANDLE FULL STACK TO PUSH
        last_stack = list(self.stack_list)[self.stacks-1];
        if len(last_stack) >= self.capacity:
            self.stack_list.append(deque([]));
            self.stacks += 1;
            last_stack = list(self.stack_list)[self.stacks-1];
        # APPEND LEFT THE NEW VALUE
        last_stack.appendleft(value);
        return;
       
    def pop(self):
        pop_element = None;
        # HANDLE EMPTY LIST OF STACKS
        if self.stacks == 0 or not bool(self.stack_list):
            return pop_element;
        # HANDLE LAST ITEM ON STACK
        first_stack = list(self.stack_list)[0];
        if len(first_stack) <= 1:
            self.stack_list.popleft();
            self.stacks -= 1;
        pop_element = first_stack.popleft();
        return pop_element;

    # TODO VALIDATE IMPLEMENTATION
    def popAt(self, index:int):
        pop_element = None;
        stack_count = 0;
        elements_count = 0;
        for stack in self.stack_list:
            stack_count += 1;
            for _ in stack:
                if stack_count+elements_count == index:
                    pop_element = list(list(self.stack_list)[stack_count]).pop(elements_count);
                    return pop_element;
                elements_count+=1;
            elements_count = 0;
        return pop_element;

    def display(self):
        print("\nCOUNT [" +  str(self.stacks) + "] \n=> " + str(self.stack_list));
# ---------------------------------------------------------------------------------- #

''' MyQueue CLASS
    v1 O(n) = We need iterate in 1 operation, either push() or pop() through all the stack, the remaining
              operation will have a O(1) time complexity.
    v2 O(1) = Reversing the stack will give you the first item stacked at the top. No need of 2 stacks then
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
'''
class MyQueue:
    def __init__(self):
        self.stack1 = deque([]);
        self.stack2 = deque([]);

    def push(self, value):  # O(N)
        self.stack1.appendleft(value);  # [1,2,3] -> [3,2,1]
        for x in self.stack1:
            self.stack2.appendleft(x);  # [3,2,1] -> [1,2,3]
        return;
    
    def pop(self):  # O(1)
        self.stack1.pop();  # NOTE: Not valid on a real stack implementation
        return self.stack2.popleft();   #  1 <- [1,2,3]
    
    def display(self):
        print( '\nStack: ' + str(list(self.stack1)));
        
# ---------------------------------------------------------------------------------- #
''' sortStack(stack) -> stack
    v1 O(n): Not the best implementation, but using deque the stack can be transformed and using
             the Python in-built method sorted() this can be arranged and returned. 

Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty

https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
'''
def top(stack:list):
    return stack[len(stack)-1]

def sortStack ( stack:list ):
    tmp_stack = [];
    while len(stack) != 0: 
        tmp = top(stack);
        stack.pop();
        while len(tmp_stack) != 0 and top(tmp_stack) > tmp:
            stack.append(top(tmp_stack));
            tmp_stack.pop();
        tmp_stack.append(tmp);
    print(tmp_stack);
    return tmp_stack;
# ---------------------------------------------------------------------------------- #
''' AnimalShelter CLASS
    v1 O(dogs + cats + shelter) increase list spaces: Space costly but efficient, keeping track on the animal type added
    v2 O(dogs + cats) using timestamps: This will require to create 
                      an Animal CLASS where storing the CREATION TIMESTAMP of the object. Then simply compare the oldest.

                      import datetime;
                      datetime = datetime.datetime.now()    # 2020-07-15 14:30:26.159446
                      timestamp = datetime.timestamp()      # 1594823426.159446

Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.
'''
class AnimalShelter: 
    def __init__(self):
        self.dogs = deque();
        self.cats = deque();
        self.shelter_order = deque();
        return;

    def enqueue(self, animal:str, name:str):
        if animal == 'dog':
            self.dogs.append(name);                
        if animal == 'cat':
            self.cats.append(name);
        self.shelter_order.append(animal);
        return;
    
    def dequeueAny(self):
        if self.shelter_order.popleft() == 'dog':
            if not bool(self.dogs):
                return;
            return self.dogs.popleft();
        if self.shelter_order.popleft() == 'cat':
            if not bool(self.cats):
                return;
            return self.cats.popleft();

    def dequeueDog(self):
        if not bool(self.dogs):
                return;
        self.shelter_order.popleft();
        return self.dogs.popleft();
    
    def dequeueCat(self):
        if not bool(self.cats):
                return;
        self.shelter_order.popleft();
        return self.cats.popleft();
    
    def display(self):
        print('Dogs: ' + str(list(self.dogs)) + ' \nCats: ' + str(list(self.cats)));




def main():
    # ----------------------------------------------------------------- #
    ''' # AnimalShelter CLASS
    animalShelter = AnimalShelter();
    animalShelter.enqueue('dog','Scooby');
    animalShelter.enqueue('dog','Pluto');
    animalShelter.enqueue('cat','Garfield');
    animalShelter.enqueue('cat','Tom');
    animalShelter.enqueue('cat','Felix');
    animalShelter.enqueue('dog','Blue');
    animalShelter.display()                     
    # INPUT: Dogs: ['Scooby', 'Pluto', 'Blue'] & Cats: ['Garfield', 'Tom', 'Felix']
    print(animalShelter.dequeueAny());          # RESULT: ['Scooby'] - Pointer should be at the 1st 'dog' added
    print(animalShelter.dequeueCat());          # RESULT: ['Garfield']
    print(animalShelter.dequeueDog());          # RESULT: ['Pluto']
    '''
    # ----------------------------------------------------------------- #
    ''' # sortStack()
    sortStack([34, 3, 31, 98, 92, 23])
    '''
    # ----------------------------------------------------------------- #
    ''' # MyQueue CLASS
    myQueue= MyQueue();
    for x in [1,2,3]:
        myQueue.push(x);
    myQueue.display();      # INPUT: Items get sorted as stack (LIFO) [3,2,1]
    print(myQueue.pop());   # RESULT: But we get the 1st item as a QUEUE (FIFO) [1]
    '''
    # ----------------------------------------------------------------- #
    ''' # SetOfStacks CLASS
    setOfStack = SetOfStack(3);
    for x in range(0,10):
        setOfStack.push(x);
    setOfStack.display();
    print(setOfStack.popAt(4));
    for x in range(4):
        setOfStack.pop();
    setOfStack.display();
    '''
    # ----------------------------------------------------------------- #
    ''' # StackMin CLASS
    stack_min = StackMin();
    for x in [23,56,78,2,89]:
        stack_min.push(x);
    stack_min.display();     # INPUT: [89, 2, 78, 56, 23]
    print(stack_min.min());     # OUTPUT: 2
    '''
    
    
    return;
main();