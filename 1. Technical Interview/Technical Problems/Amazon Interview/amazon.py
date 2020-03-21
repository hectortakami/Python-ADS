from functools import reduce
print("\n\n******************************** AMAZON Q&A ********************************\n")
# 
# 
'''
PROBLEM 1:  Given a collection of numbers, retreive the 
            two numbers (if theres any) that sum a given target value
'''
# INPUT:  
#             1. [1, 2, 3, 9] , target = 8
#             2. [1, 2, 4, 4] , target = 8
# OUTPUT:
#             1. False
#             2. True

def matchingPair(arr, target): # O(n)
    values = {}
    for i in range(0, len(arr)):
        if (target - arr[i]) in values:
            return True
        values[arr[i]] = i
    return False

print(' matchingPair([1,2,3,9], 8)\n => ' + str(matchingPair([1,2,3,9], 8)))
print(' matchingPair([1,2,4,4], 8)\n => ' + str(matchingPair([1,2,4,4], 8)) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 2:  Determine if two strings are anagrams (you can construct 
            the other by changing the position of it's letters)
'''
# INPUT:  
#             1. 'SILENT', 'LISTEN'
#             2. 'DOG', 'DOGGY'
#             3. 'TRIANGLE', 'INTEGRAL'
# OUTPUT:
#             1. True
#             2. False
#             3. True

def isAnagram(str1, str2): # O(1)
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    if str1 == str2:
        return True
    else:
        return False

print(' isAnagram(\'SILENT\', \'LISTEN\')\n => ' + str(isAnagram('SILENT', 'LISTEN')))
print(' isAnagram(\'DOG\', \'DOGGY\')\n => ' + str(isAnagram('DOG', 'DOGGY')))
print(' isAnagram(\'TRIANGLE\', \'INTEGRAL\')\n => ' + str(isAnagram('TRIANGLE', 'INTEGRAL')) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 3:  Given 2 strings that represent a number, sum the 
            two numbers and return the result as a string
'''
# INPUT:    '12', '13'
# OUTPUT:   '25'

def sum2strings(str1, str2): # O(1)
    sum = int(str1) + int(str2)
    return str(sum)

print(' sum2strings(\'12\', \'13\')\n => \'' + sum2strings('12', '13') + '\'\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 4:  Given an array that contains both positive 
            and negative integers, find the k pairs of 
            distinct elements which are the maximum product 
            of such array.
'''
# INPUT:    
#           1. [-5,-2,-3,-1,1,2,3], k = 3
#           1. [1, 4, 3, 6, 7, 0], k = 1
#           1. [-1, -3, -4, 2, 0, -5], k = 2

# OUTPUT:   
#           1. [-5,-3], [-5,-2], [2,3]
#           2. [6, 7]
#           3. [-4, -5], [-3, -5]
# EXPLANATION: 
#           1. K = 3 so we retreive the 3 most significant answers
#              [-5 * -3] = 15, [-5 * -2] = 10, [2 * 3] = 6

def maxProductPairs(arr, k): # O(n^2)
    result = []
    mulDict = {}
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                pass
            else:
                mulDict[(arr[i] * arr[j])] = [arr[j], arr[i]]
    for key in reversed(sorted(mulDict.keys())):
        if k > 0:
            result.append(mulDict.get(key))
            k-=1
        else:
            break
    return result
        
        
print(' maxProductPairs([-5,-2,-3,-1,1,2,3], 3)\n => \'' + str(maxProductPairs([-5,-2,-3,-1,1,2,3], 3)))
print(' maxProductPairs([1, 4, 3, 6, 7, 0], 1)\n => \'' + str(maxProductPairs([1, 4, 3, 6, 7, 0], 1)))
print(' maxProductPairs([-1, -3, -4, 2, 0, -5], 2)\n => \'' + str(maxProductPairs([-1, -3, -4, 2, 0, -5], 2)) + '\'\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 5:  Given an n x n matrix and a number x, 
            find the position of x in the matrix if it is 
            present in it. Otherwise, print “Not Found”. 
            In the given matrix, every row and column is sorted 
            in increasing order. The designed algorithm should 
            have linear time complexity.
'''
# INPUT:    
#           1. mat[4][4] = [ [10, 20, 30, 4],
#                            [15, 25, 35, 45],
#                            [27, 29, 37, 48],
#                            [32, 33, 39, 50]  ];
#               x = 29
# OUTPUT:   
#           1. Found at (2, 1)

def searchInMatrix(matrix, target): # O(n)
    # O (n^2)
    # for row in range(0, len(matrix)):
    #     for column in range(0, len(matrix[0])):
    #         if matrix[row][column] == target:
    #             return 'Found at ' + str([row, column])
    # return 'Element not found'
    rowIdx = 0
    colIdx = len(matrix) - 1 # Start searching on the top right item
    while rowIdx < len(matrix) - 1 and colIdx >= 0:
        # Keep the loop until reach the end of the rows or the beginnig of the columns
        if matrix[rowIdx][colIdx] == target:
            return 'Found at ' + str([rowIdx, colIdx])
        elif matrix[rowIdx][colIdx] > target:
            # If we found a greater value go one column left
            colIdx -= 1
        else:
            # If we found a lesser value go one row down
            rowIdx += 1
    return 'Element not found'

print(''' searchInMatrix( [  [10, 20, 30, 4],
                    [15, 25, 35, 45],
                    [27, 29, 37, 48],
                    [32, 33, 39, 50]  ], 29)\n => ''' + searchInMatrix( [[10, 20, 30, 4],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]], 29) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 6:  Given an array that contains both positive and negative
            integers, find the product of the maximum product subarray. 
            Expected Time complexity is O(n) and only O(1) extra space can be used
'''
# INPUT:    
#           1. [6, -3, -10, 0, 2]
#           2. [-1, -3, -10, 0, 60]
#           3. [-2, -3, 0, -2, -40]
# OUTPUT:   
#           1. [6, -3, -10] => 180
#           2. [60] => 60
#           3. [-2, -40] => 80

def maxMulSubarray(arr):  # O(n)
    maxSubArr = []
    maxMul = 0

    startIdx = 0
    endIdx = startIdx + 1
    while startIdx < len(arr):
        subArr = arr[startIdx:endIdx]
        subMul = reduce((lambda x, y: x * y), subArr)
        if subMul > maxMul:
            maxMul = subMul
            maxSubArr = subArr
        if endIdx < len(arr):
            endIdx += 1
        else:
            startIdx += 1
            endIdx = startIdx + 1

    return str(maxSubArr) + ' = ' + str(maxMul)

print(' maxMulSubarray([6, -3, -10, 0, 2])\n => ' + maxMulSubarray([6, -3, -10, 0, 2]))
print(' maxMulSubarray([-1, -3, -10, 0, 60])\n => ' + maxMulSubarray([-1, -3, -10, 0, 60]))
print(' maxMulSubarray([-2, -3, 0, -2, -40])\n => ' + maxMulSubarray([-2, -3, 0, -2, -40]) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 7:  Given a string, find the longest substring which is palindrome
'''
# INPUT:    
#           1. “forgeeksskeegfor”
# OUTPUT:   
#           1. “geeksskeeg”

def longestPalindrome(word): # O(n)
    maxPalindrome = ''
    startIdx = 0
    endIdx = startIdx + 1
    while startIdx < len(word):
        subWord = word[startIdx:endIdx]
        backSubWord = subWord[::-1]
        if subWord == backSubWord and len(subWord) > len(maxPalindrome):
            maxPalindrome = subWord
        if endIdx < len(word):
            endIdx += 1
        else:
            startIdx += 1
            endIdx = startIdx + 1
    return maxPalindrome if maxPalindrome != '' else 'No palindrome found'

print(' longestPalindrome(\'forgeeksskeegfor\')\n => ' + longestPalindrome('forgeeksskeegfor') + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 8:  Convert an int number into it's own 
            writable representation (constrainted to thousands)
'''
# INPUT:    
#           1. 2310
#           2. 44962
# OUTPUT:   
#           1. 'two thousand three hundred and ten'
#           2. 'forty four thousand nine hundred and sixty two '

def num2word(num): # O(1)
    numStr = ''
    unit_dict = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ", "ten "]
    ten_dict = ["", "eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
    dec_dict = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]
    
    thousand = num // 1000
    hundred = (num % 1000) // 100
    unit = num % 100

    if thousand > 0:
        if thousand < 10:
            numStr += unit_dict[thousand] + 'thousand '
        if thousand >= 10 and thousand < 20:
            numStr += ten_dict[thousand//10] + 'thousand '
        if thousand >= 20 and thousand < 100:
            numStr += dec_dict[thousand // 10] + unit_dict[thousand % 10] + 'thousand '
    if hundred > 0:
        numStr += unit_dict[hundred] + 'hundred and '
    if unit > 0:
        if unit <= 10:
            numStr += unit_dict[unit]
        if unit > 10 and unit < 20:
            numStr += ten_dict[unit % 10]
        if unit >= 20 and unit < 100:
            numStr += dec_dict[unit // 10] + unit_dict[unit % 10]
    return numStr


print(' num2word(2310)\n => '  +  num2word(2310))
print(' num2word(44962)\n => '  +  num2word(44962) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 8:  Given a string retrieve the k more repeating characters in the string

'''
# INPUT: 'We are all peaceful soul and blissful soul and loveful soul happy soul', k = 5
# OUTPUT: ['l', 'u', 's', 'a', 'o']

def mostRepeatedChar(phrase, k): # O(n)
    chars = list(phrase.lower().replace(' ', ''))
    charDict = {}
    for char in chars:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    mostRepeated = []
    for item in reversed(sorted(charDict.items(), key=lambda kv: (kv[1], kv[0]))):
        if (k <= 0):
            return mostRepeated
        mostRepeated.append(item[0])
        k -= 1

print(' mostRepeatedChar(\'We are all peaceful soul and blissful soul and loveful soul happy soul\', 5)\n => '  +  str(mostRepeatedChar('We are all peaceful soul and blissful soul and loveful soul happy soul', 5)) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 9:  Given 2 arrays, create a function that let's a user know (True / False)
            whether these two arrays contain any common items

'''
# INPUT: 
#           1. ['a', 'b', 'c', 'x'], ['z', 'y', 'i']
#           2. ['a', 'b', 'c', 'x'], ['z', 'y', 'x']
# OUTPUT: 
#           1. False
#           2. True

def containCommonChars(arr1, arr2): # O(n)
    for item in arr1:
        if item in arr2:
            return True
    return False

print(' containCommonChars([\'a\', \'b\', \'c\' \'x\'], [\'z\', \'y\', \'i\'])\n => '  +  str(containCommonChars(['a', 'b', 'c', 'x'], ['z', 'y', 'i'])))
print(' containCommonChars([\'a\', \'b\', \'c\' \'x\'], [\'z\', \'y\', \'x\'])\n => '  +  str(containCommonChars(['a', 'b', 'c','x'], ['z', 'y', 'x'])) + '\n\n')

# -------------------------------------------------------------------------------------------

'''
PROBLEM 9:  Given a 2d grid map of '1's (land) and '0's (water), 
            count the number of islands. An island is surrounded 
            by water and is formed by connecting adjacent lands 
            horizontally or vertically. You may assume all four 
            edges of the grid are all surrounded by water.

'''
# INPUT: 
#           1.  11110
#               11010
#               11000
#               00000
# 
#           2.  11000
#               11000
#               00100
#               00011
# OUTPUT: 
#           1. 1 island 
#           2. 3 islands

def __isIsland(x, y, grid):
    # top = grid[x][y - 1] 
    # bottom = grid[x][y + 1]
    # left = grid[x - 1][y]
    # right = grid[x + 1][y]
    return
        



def numIslands(grid):
    for row in range(0, len(grid)):
        for column in range(0, len(grid[0])):
            if grid[row][column] == 1:
                __isIsland(row, column, grid)
            
numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])


            
        



print("\n******************************** AMAZON Q&A ********************************\n\n")
