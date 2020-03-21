# -------------------------------------------------------------------------
# PROBLEM 1: You are a professional robber planning to rob houses along a street. 
#            Each house has a certain amount of money stashed, the only constraint 
#            stopping you from robbing each of them is that adjacent houses have 
#            security system connected and it will automatically contact the police 
#            if two adjacent houses were broken into on the same night.
#            Given a list of non-negative integers representing the amount of 
#            money of each house, determine the maximum amount of money you can 
#            rob tonight without alerting the police.
# INPUT: 
#       1. [1,2,3,1]
#       2. [2,7,9,3,1]
# OUTPUT: 
#       1. 4 => ([house-1] = 1) + ([house-3] = 3) = 4
#       2. 12 => ([house-1] = 2) + ([house-3] = 9) + ([house-5] = 1) = 12
# EXPLANAITION:
#       We cannot rob 2 continous houses so we need to traverse by odds or even
#       houses the array and find the greatest amount summing each of their values
# -------------------------------------------------------------------------

def rob(houses): # O( n )
    evenCount,oddCount = 0,0
    for i in range(0, len(houses)):
        # It's an even numbers
        if i % 2 == 0:
            evenCount += houses[i]
        else:
            # It's an odd numbers
            oddCount += houses[i]
    if evenCount > oddCount:
        return evenCount
    return oddCount


def main():
    print('\n rob([1,2,3,1])\n => ' + str(rob([1,2,3,1])))
    print(' rob([1,2,3,1])\n => ' + str(rob([2, 7, 9, 3, 1])))
main()