print("\n\n\n***************** QUICK SORT IMPLEMENTATION *****************\n")

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot (last element)

    for j in range(low , high):   
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): # O (n log n) || O ( n^2 ) in worst case
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        partition_index = partition(arr,low,high) 

        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, partition_index-1) 
        quickSort(arr, partition_index+1, high) 


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(' Unsorted array:    ' + str(numbers))
quickSort(numbers, 0, len(numbers)-1)
print('\n => QuickSort:\n\t\t    ' + str(numbers))

print("\n\n***************** QUICK SORT IMPLEMENTATION *****************\n\n\n")

