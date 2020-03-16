print("\n\n***************** DYNAMIC PROGRAMMING *****************\n")

# This is a function that returns 
# another function so we can 
# locaclly ENCAPSULATE THE CACHE
def memoizedFunction():
    # LOCAL DECLARED CACHE
    cache = {}
    # Another function declaration
    def addTo10(num):
        if num in cache:
            print('Already know this value, returning it from cache! :)')
            return cache[num]
        else:
            print('Storing value in cache, for 1st time!')
            cache[num] = num + 10
            return cache[num]

    return addTo10 # Return the function with the local cache scope


memoized = memoizedFunction()

memoized(5)
memoized(5)
memoized(5)



print("\n***************** DYNAMIC PROGRAMMING *****************\n\n")
