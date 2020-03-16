print("\n\n***************** DYNAMIC PROGRAMMING *****************\n")

# GLOBAL DECLARED CACHE
cache = {}
# Simple function that adds 10 to the input
def memoizedAddTo10(num):
    if num in cache:
        # If we already have processed the input given, we just look for the result in the
        # cache, without need to re-compute the result
        print('--> We already compute it, find it in cache :)')
        return cache[num] #O(1)
    else:
        # If the operation demands a lot of processing theres no need to do it again
        # We just process it once, and save the value to the hash table
        print('-> Dont have the value yet, let\'s process it and save it in the cache!\n')
        cache[num] = 10 + num
        return cache[num]

memoizedAddTo10(15) # O( Operation ) only the first time
memoizedAddTo10(15) # O( 1 )
memoizedAddTo10(15) # O( 1 )
memoizedAddTo10(15) # O( 1 )

print("\n***************** DYNAMIC PROGRAMMING *****************\n\n")
