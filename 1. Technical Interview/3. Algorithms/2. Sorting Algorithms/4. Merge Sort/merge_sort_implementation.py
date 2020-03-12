print("\n\n\n***************** MERGE SORT IMPLEMENTATION *****************\n")

def merge(left, right):
    mergeArr = [] # This is the resulting list where the values will be sorted
    # Keeps track of the indexes of each half array
    leftIdx = 0
    rightIdx = 0
    while (leftIdx < len(left) and rightIdx < len(right)):
        # Do comparations between lists
        if (left[leftIdx] < right[rightIdx]):
            # If the fist value from left list is minor than the first value in 
            # right list it will be appended to the result array first
            mergeArr.append(left[leftIdx])
            leftIdx+=1
        else:
            # Otherwise, the first value on right list is minor than the first value in 
            # left list we append it to the result
            mergeArr.append(right[rightIdx])
            rightIdx += 1
    # If we dont have more items to compare, it means that we end one of the two lists
    # we return the result array with the values sorted + the rest of the values in the
    # other arrays
    return mergeArr + left[ leftIdx : len(left) ] + right[rightIdx: len(right)]

def mergeSort(arr):  # O(n log n)
    if len(arr) == 1:
        # If we only have a one element array just return it
        return arr
    # Split the array into 2 parts
    # Left Half
    leftArray = arr[0:(len(arr) // 2)]
    # Right Half
    rightArray = arr[(len(arr) // 2):len(arr)]

    # Merge both list into one sorted 
    return merge(
        # Recursevely return the value of each half evaluated
        mergeSort(leftArray),
        mergeSort(rightArray)
        )

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(' Unsorted array:    ' + str(numbers))

print('\n => MergeSort:\n\t\t    ' + str(mergeSort(numbers)))

print("\n***************** MERGE SORT IMPLEMENTATION *****************\n")

