print("\n\n\n***************** RECURSION Q&A *****************\n")

# -------------------------------------------------------------------------
# PROBLEM 1: Write a function that finds the factorial of any number.
# INPUT: 5
# OUTPUT: 120
# EXPLANATION: 5! = 5 * 4 * 3 * 2 * 1 = 120
# -------------------------------------------------------------------------

def factorial(num): # O(n)
    # Base Case 1! = 1
    if num == 1:
        return 1
    # Recursive Call, num * (num-1)!
    return num * factorial( num-1 )
    
# -------------------------------------------------------------------------
# PROBLEM 2: Given an index return the value associated of the Fibonacci sequence
# INPUT: 7
#           0  1  2  3  4  5  6  7
# OUTPUT: [ 0, 1, 1, 2, 3, 5, 8, 13 ] => 13
# EXPLANATION: The patter is that each value correspons to the sum of the 2
#              previous values: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# -------------------------------------------------------------------------

def fibonacci(index): # O(2^n)
    # Base Case | fib(0) = 0 and fib(1) = 1
    if index <= 1:
        return index
    # Recursive Call, fib( n-2 ) + fib( n-1 )
    return fibonacci(index-2) + fibonacci(index-1)

def fibonacciIterative(index):  # O (n)
    # In this case this solution is more optimal than the recursive approach
    # doing fibonacci(40) using recursive method will demand a lot of time
    arr = [0, 1] # This is the started numbers of the sequence
    for i in range(2, index + 1):
        # We append the next value in the fibonacci sequence
        arr.append(arr[i - 2] + arr[i - 1])
    # Retreive the item searched at that index
    return arr[index]

# -------------------------------------------------------------------------
def main():
    print(' factorial(5) ')
    print(' => ' + str(factorial(5)))
    print(' factorial(1) ')
    print(' => ' + str(factorial(1)))
    print(' factorial(20) ')
    print(' => ' + str(factorial(20)))

    print('\n fibonacci(7) ')
    print(' => ' + str(fibonacci(7)))
    print(' fibonacci(10) ')
    print(' => ' + str(fibonacci(10)))
    print(' fibonacci(12) ')
    print(' => ' + str(fibonacci(12)))

    # fibonacci(40) will be almost impossible to compute because it grows 
    # exponentially to 2^n demanding 2^40 computations that's why it's 
    # better the iterative approach O(n)
    print('\n fibonacciIterative(40) ')
    print(' => ' + str(fibonacciIterative(40)))

    # -------------------------------------------------------------------------
main()

print("\n***************** RECURSION Q&A *****************\n\n")
