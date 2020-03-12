print("\n\n\n***************** BUBBLE SORT IMPLEMENTATION *****************\n")

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return

def bubbleSort(arr):  # O( n^2 )
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                # If we found a value on the left that is greater than the following
                # on the right we swap them
                swap(arr, i, j)
            


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(' Unsorted array: ' + str(numbers))
bubbleSort(numbers)
print('\n => BubbleSort:\n\t\t ' + str(numbers))
print("\n***************** BUBBLE SORT IMPLEMENTATION *****************\n")
