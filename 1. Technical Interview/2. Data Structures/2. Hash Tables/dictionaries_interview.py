print("\n\n******************** HASH TABLES Q&A ********************\n")

# -------------------------------------------------------------------------
# PROBLEM 1: Given an array, returns the first recurring item
#            (the first item repeated in an array)
# INPUT:
#   1. [2,5,1,2,3,5,1,2,4]
#   2. [2,1,1,2,3,5,1,2,4]
#   3. [2,3,4,5]
#   4. [2,5,5,2,3,5,1,2,4]
# OUTPUT:
#   1. 2
#   2. 1
#   3. None
#   4. 5
# -------------------------------------------------------------------------


def firstRecurringCharacter(data):
    numsDict = {}
    for num in data:  # O(n)
        if num in numsDict:
            print(' => ' + str(num))
            return num
        numsDict[num] = 1

    print(' => None ')
    return None


# -------------------------------------------------------------------------
# PROBLEM 2: Similarly to the previous excercise retreive the first recurring
#            character, but only when it is compared with the rest of the array
# INPUT: [2,5,5,2,3,5,1,2,4]
# OUTPUT: 2
# -------------------------------------------------------------------------

def firstRecurringRest(data):
    for idx, num in enumerate(data):  # O(n)
        subArray = data[slice(idx + 1, len(data))]
        subArrayDict = dict.fromkeys(subArray)
        if num in subArrayDict:
            print(' => ' + str(num))
            return num

    print(' => None')
    return None

# -------------------------------------------------------------------------
# PROBLEM 2: Given 2 arrays, create a function that returns true/false
#            whether any of these two arrays contains common items
# INPUT:
#   1. ['a', 'b', 'c']
#      ['1', '2', '3']
#   2. ['a', 'b', 'x']
#      ['1', '2', 'x']
# OUTPUT: 2
#   1. false
#   2. true
# -------------------------------------------------------------------------


def containsCommonItems(arr1, arr2):
    arr1Dict = dict.fromkeys(arr1)
    arr2Dict = dict.fromkeys(arr2)
    for item in arr1Dict:  # O(n)
        if item in arr2Dict:
            print(' => True')
            return True
    print(' => False')
    return False


# -------------------------------------------------------------------------
def main():

    print(' firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4]) ')
    firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4])
    print(' firstRecurringCharacter([2,1,1,2,3,5,1,2,4]) ')
    firstRecurringCharacter([2, 1, 1, 2, 3, 5, 1, 2, 4])
    print(' firstRecurringCharacter([2,3,4,5]) ')
    firstRecurringCharacter([2, 3, 4, 5])
    print(' firstRecurringCharacter([2,5,5,2,3,5,1,2,4]) ')
    firstRecurringCharacter([2, 5, 5, 2, 3, 5, 1, 2, 4])

    print('\n firstRecurringRest([2,5,5,2,3,5,1,2,4]) ')
    firstRecurringRest([2, 5, 5, 2, 3, 5, 1, 2, 4])

    print(
        '\n containsCommonItems([\'a\', \'b\', \'c\'], [\'1\', \'2\', \'3\']) ')
    containsCommonItems(['a', 'b', 'c'], ['1', '2', '3'])
    print(
        ' containsCommonItems([\'a\', \'b\', \'x\'], [\'1\', \'2\', \'x\']) ')
    containsCommonItems(['a', 'b', 'x'], ['1', '2', 'x'])


main()
print("\n******************** HASH TABLES Q&A ********************\n\n")
