import time
import string

print("\n\n\n***************************************\n")
start = time.time()  # Time start to be meausure
# ------------------------------------------------
# BIG O - SCALABILITY PATTERNS
# ------------------------------------------------

# ------------------------------------------------
# O(1) Complexity -> Constant Time
# ------------------------------------------------
b = []
b.append("item")
# ------------------------------------------------

# ------------------------------------------------
# O(n) Complexity -> Linear Time
# ------------------------------------------------
a = [1, 2, 3, 4, 5]
for i in a:
    print(i * 2)
# ------------------------------------------------

# ------------------------------------------------
# O(n + m) -> Linear Time
# ------------------------------------------------
a = [1, 2, 3, 4, 5]
b = ['1', '2', '3', '4', '5']
for x in a:
    # a as the n input to iterate
    print(x)
for x in b:
    # b as the m input to iterate
    print(x)
#
# NOTE: They might have the same length but they are
# AT THE SAME LEVEL OF IDENTATION thats why we add them
# ------------------------------------------------

# ------------------------------------------------
# O(n^2) -> Quadratic Time
# ------------------------------------------------


def getAllCombinations(array):
    for i in range(0, len(array)):  # O(n)
        for j in range(0, len(array)):  # O(n)
            print(array[i] + " " + array[j])


getAllCombinations(['a', 'b', 'c', 'd', 'e'])
# NOTE: In NESTED LOOPS we MULTIPLY the number
# of inputs -> O(n) * O(n) = O(n^2)
# ------------------------------------------------

# Time stops the measurement
print("\t" + str(time.time() - start) + " seconds")
print("\n***************************************\n\n\n")
