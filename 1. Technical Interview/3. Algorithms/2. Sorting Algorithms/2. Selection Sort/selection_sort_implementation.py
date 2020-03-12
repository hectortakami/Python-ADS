print("\n\n\n***************** SELECTION SORT IMPLEMENTATION *****************\n")

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return

def selectionSort(arr):  # O( n^2 )
    min_idx = 0 # Keeps track of the index to be swap
    for i in range(0, len(arr)):
        min_num = arr[i] # Defines the minimum value found in the iteration
        for j in range(i + 1, len(arr)):
            # If we found a number less than the min_num we store
            # it's value and index until the iteration ends
            if arr[j] < min_num:
                min_idx = j
                min_num = arr[j]
        # If we reach at the end of the sub-array iteration we swap 
        # the values of the index we are located with the minimum value
        # found in the following sub-array
        swap(arr, i, min_idx)
            
        
            


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(' Unsorted array:    ' + str(numbers))
selectionSort(numbers)
print('\n => SelectionSort:\n\t\t    ' + str(numbers))
print("\n***************** SELECTION SORT IMPLEMENTATION *****************\n")
