print("\n\n***************** DYNAMIC PROGRAMMING Q&A *****************\n")
# -------------------------------------------------------------------------
# PROBLEM 1: Define an improve method of fibonacci algorithm 
#            using caching (memoization) to store the previous values and
#            retreive a better performance
# INPUT: 7
# OUTPUT: 0 1 1 2 3 5 8 13 => 13
# -------------------------------------------------------------------------

def memoizeFibonacci(): # O(n)
    cache = {0:0, 1:1} # Fill the cache with the base cases just to be more efficient 
    def fibonacci(idx):
        # 1rst memoizedFib(10) -> O(n) The first computation
        # 2nd memoizedFib(10) -> O(1) The second time we look for the value
        if idx in cache:
            return cache[idx]
        else:
            cache[idx] = fibonacci(idx - 2) + fibonacci(idx - 1)
            return cache[idx]
    return fibonacci


memoizedFib = memoizeFibonacci()

memoizedFib(30)
# It doesn't have to iterate recursevely until find the 50th value in the sequence
# it only goes back to the last value compute in the cache, that is '30', grabs it
# and then compute the rest, optimizing the algorithm to need to compute less than the
# 50% of the recursive calls to retreive the answer
result = memoizedFib(50) 

def main():
    print(' memoizedFib( 50 )\n => ' + str(result))
main()

print("\n***************** DYNAMIC PROGRAMMING Q&A *****************\n\n")
