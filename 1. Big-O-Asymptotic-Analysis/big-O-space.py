print("\n\n\n***************************************\n")
# ------------------------------------------------
# BIG O - SPACE COMPLEXITY PATTERNS
# ------------------------------------------------

# ------------------------------------------------
# O(1) Complexity -> Constant Space Allocation
# ------------------------------------------------


def printBoo(n):
    for i in n:  # O(1)
        print("Boo")


printBoo([1, 2, 3, 4, 5])
# NOTE: We only have one variable assignment
# (i index in the for loop)
# ------------------------------------------------

# ------------------------------------------------
# O(n) Complexity -> Linear Space Allocation
# ------------------------------------------------


def assignHi(n):
    array = []  # O(1)
    for i in range(0, n):  # O(n)
        array.append('hi')  # O(1)
    return array


print(assignHi(7))
# ------------------------------------------------
print("\n***************************************\n\n\n")
