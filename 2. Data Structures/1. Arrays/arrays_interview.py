import collections
print("\n\n\n***************** ARRAYS Q&A *****************\n")

# -------------------------------------------------------------------------
# PROBLEM 1: Create a function that reverses a string
# INPUT: 'Hi my name is Hector'
# OUTPUT: 'rotceH si eman ym iH'
# -------------------------------------------------------------------------


def reverseString(str):  # O(1)

    if (type(str) is not type('')):
        print('\nError: Invalid String\n')
        return
    elif (len(str) == 1):
        print(' =>' + str)
        return
    else:
        # ANSWER 1
        # Reverse For Loop
        '''
        strReversed = ''
        for i in range(len(str)-1, -1, -1):
            strReversed += str[i]
        print(' => ' + strReversed)
        return
        '''

        # ANSWER 2
        # Slice the string starting at the end of the string and move backwards
        print(' => ' + str[::-1])
        return


# -------------------------------------------------------------------------
# PROBLEM 2: Given 2 sorted arrays merge them to create one sorted array
# INPUT:
#   1: [0, 3, 4, 31]
#   2: [4, 6, 30]
# OUTPUT: [0, 3, 4, 4, 6, 30, 31]
# -------------------------------------------------------------------------


def mergeSorted(arr1, arr2):  # O(n)

    if len(arr1) == 0:
        print(' => ' + str(arr2))
        return
    if len(arr2) == 0:
        print(' => ' + str(arr1))
        return

    mergeArray = (arr1 + arr2)
    mergeArray.sort()

    print(' => ' + str(mergeArray))
    return mergeArray


# -------------------------------------------------------------------------
# PROBLEM 3: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# INPUT: [2, 4, 7, 15], target = 9
# OUTPUT: [0, 2] => arr[0] + arr[2] => 2 + 7 = 9
# -------------------------------------------------------------------------


def twoSum(data, target):
    # ANSWER 1
    # O(n^2)
    # Iterate looking for all occurences that sum exaclty the target value
    '''
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if (data[i] + data[j] == target):
                print(' => ' + str([i, j]))
                return [i, j]
            pass
        pass
    print('\nNo coincidences found\n')
    '''
# INPUT: [2, 4, 7, 15], target = 9
# OUTPUT: [0, 2] => arr[0] + arr[2] => 2 + 7 = 9
    numsDict = {}
    for idx, num in enumerate(data):
        # We store in the dictionary the [number: position_idx]
        numsDict[num] = idx

    for numKey in numsDict:
        # We ask if there is any key complementary that we're situated can give us the target value
        if (target - numKey) in numsDict:
            print(' => ' + str([numsDict.get(numKey),
                                numsDict.get((target - numKey))]))
            # Retreive the values (position_idx) of the keys found
            return [numsDict.get(numKey), numsDict.get((target - numKey))]

    print('\nNo coincidences found\n')
    return []


# -------------------------------------------------------------------------
# PROBLEM 4: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# INPUT: [-2,1,-3,4,-1,2,1,-5,4]
# OUTPUT: 6
# Explanaition: [4,-1,2,1] has the largest sum = 6.
# -------------------------------------------------------------------------


def maxSubArray(data):
    # ANSWER 1
    # O(n^2)
    # Iterating through all sub arrays possible
    '''
    maxValue = 0
    for start in range(0, len(data)):
        for end in range(start + 1, len(data)):
            # Splice [start : end : steps]
            subArraySum = sum(data[start:end])
            if (subArraySum > maxValue):
                maxValue = subArraySum
            pass
        pass

    print(' => ' + str(maxValue))
    return maxValue
    '''
    # ANSWER 2
    # O(n)
    # Compare using dynamic programing the sums
    maxSubArraySum = data[0]
    currentMax = data[0]
    for i in range(1, len(data)):
        currentMax = max(data[i], currentMax + data[i])
        maxSubArraySum = max(maxSubArraySum, currentMax)

    print(' => ' + str(maxSubArraySum))
    return maxSubArraySum


# -------------------------------------------------------------------------
# PROBLEM 4: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# INPUT: [0,1,0,3,12]
# OUTPUT: [1,3,12,0,0]
# -------------------------------------------------------------------------


def moveZeros(data):  # O(n)
    zerosArray = collections.deque([])
    # [0, 1, 0, 3, 12]
    for value in reversed(data):
        if (value != 0):
            zerosArray.appendleft(value)
        else:
            zerosArray.append(value)

    print(' => ' + str(zerosArray))
    return zerosArray


# -------------------------------------------------------------------------
# PROBLEM 5: Given an array of integers, find if the array contains any duplicates.
# INPUT:
#   1. [1,2,3,1]
#   2. [1,2,3,4]
#   3. [1,1,1,3,3,4,3,2,4,2]
# OUTPUT:
#   1. true
#   2. false
#   3. true
# -------------------------------------------------------------------------


def containsDuplicate(data):  # O(n)
    haveDuplicates = False
    myDictionary = dict()  # { '1':2 , '2':1 , '3':1 }

    for value in data:
        if value in myDictionary:
            # We can use the dictionary to keep a value count of any occurences
            # myDictionary[value] += 1
            haveDuplicates = True
            print(' => ' + str(haveDuplicates))
            return True
        else:
            myDictionary[value] = 1

    print(' => ' + str(haveDuplicates))
    return False

# -------------------------------------------------------------------------
# PROBLEM 6: Given an array, rotate the array to the right by k steps, where k is non-negative.
# INPUT:
#   1. [1,2,3,4,5,6,7] and k = 3
#   2. [-1,-100,3,99] and k = 2
# OUTPUT:
#   1. [5,6,7,1,2,3,4]
#   2. [3,99,-1,-100]
# EXPLANATION:
#   rotate 1 steps to the right: [99, -1, -100, 3]
#   rotate 2 steps to the right: [3, 99, -1, -100]
# -------------------------------------------------------------------------


def rotateArray(data, k):  # O(n)
    data = collections.deque(data)

    for x in range(0, k):
        lastValue = data.pop()
        data.appendleft(lastValue)

    print(' => ' + str(data))
    return data


# -------------------------------------------------------------------------
# PROBLEM 7: Take the 'sen' parameter being passed and return the largest
#            word in the string. If there are two or more words that are the
#            same length, return the first word from the string with that length.
# INPUT:
#   1. "fun&!! time"
#   2. "I love dogs"
# OUTPUT:
#   1. time
#   2. dogs
# -------------------------------------------------------------------------

def longestWord(sen):  # O(n)
    words = sen.split(' ')
    maxWord = ''
    for word in words:
        # .isalpha() veryfies if all the chars in the string are alphabetic (not symbols)
        if (not word.isalpha()):
            pass
        else:
            if (len(word) > len(maxWord)):
                maxWord = word
    print(' => ' + maxWord)
    return maxWord


# -------------------------------------------------------------------------


def main():

    print(' reverseString (\'Hi my name is Hector\') ')
    reverseString('Hi my name is Hector')

    print('\n mergeSorted([0, 3, 4, 3, 100], [4, 6, 30, 50]) ')
    mergeSorted([0, 3, 4, 3, 100], [4, 6, 30, 50])

    print('\n twoSum([2, 4, 7, 15], 11) ')
    twoSum([2, 4, 7, 15], 11)

    print('\n maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) ')
    maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

    print('\n containsDuplicate([1, 2, 3, 1]) ')
    containsDuplicate([1, 2, 3, 1])
    print(' containsDuplicate([1, 2, 3, 4]) ')
    containsDuplicate([1, 2, 3, 4])
    print(' containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) ')
    containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

    print('\n moveZeros([0, 1, 0, 3, 12]) ')
    moveZeros([0, 1, 0, 3, 12])

    print('\n rotateArray([1, 2, 3, 4, 5, 6, 7], 3) ')
    rotateArray([1, 2, 3, 4, 5, 6, 7], 3)
    print(' rotateArray([-1, -100, 3, 99], 2) ')
    rotateArray([-1, -100, 3, 99], 2)

    print('\n longestWord(\'fun&!! time\') ')
    longestWord('fun&!! time')
    print(' longestWord("I love dogs") ')
    longestWord("I love dogs")


    # -------------------------------------------------------------------------
main()

print("\n***************** ARRAYS Q&A *****************\n\n")
