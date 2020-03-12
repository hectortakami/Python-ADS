print("\n\n\n***************** INSERTION SORT IMPLEMENTATION *****************\n")

def insertionSort(arr): # O (n^2)
    for i in range(1, len(arr)):
        value_to_insert = arr[i] # We store the value to insert
        insertion_idx = i - 1 # We define the index to start the lookup one place previous the value to be inserted
        for j in range(insertion_idx, -1, -1): # Iterate backwars from the value we want to insert
            if arr[j] > value_to_insert:
                # If we find a value greater than the value to be inserted
                # We store the position j - 1 to insert the value
                insertion_idx = j - 1
                # And move one position further all the greater values in the array
                arr[j + 1] = arr[j]
            else:
                # If we find a value less than the insertion we end the loop
                break
        # If we end the loop we now insert the value in the correspond index ( j + 1 )
        arr[insertion_idx + 1] = value_to_insert
        
# Note: The index is ( j + 1 ) because in the case to reach the end of the array
#       the value of j will be -1, instead of 0 because we're iterating backwards
#       one position previous to the current value to be inserted
    


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(' Unsorted array:    ' + str(numbers))
insertionSort(numbers)
print('\n => InsertionSort:\n\t\t    ' + str(numbers))

print("\n***************** INSERTION SORT IMPLEMENTATION *****************\n")
