import collections

print("\n\n\n*************** ARRAYS METHODS ***************\n")
arrayVar = collections.deque(['1', '2', '3', '4', '5'])

# ---------------------------------------------------------------------------------------

# Lookup | Access
# O(1)
valueIndex = arrayVar[3]  # -> '4'

# ---------------------------------------------------------------------------------------

# Insertion (End)
# O(1)
arrayVar.append('6')  # -> ['1', '2', '3', '4', '5', '6']
# JavaScript
# arrayVar.push('6')

# Insertion (Middle)
# O(n)
arrayVar.insert(2, 'alien')  # -> ['1', '2', 'alien', '3', '4', '6']
# JavaScript
# arrayVar.splice(2, 0, 'alien')

# Insertion (Start)
# O(n)
arrayVar.appendleft('x')  # -> ['x', '1', '2', '3', '4', '5']
# JavaScript
# arrayVar.unshift('x')

# ---------------------------------------------------------------------------------------

# Remove (End)
# O(1)
removedPop = arrayVar.pop()  # -> '6' => ['1', '2', '3', '4', '5']

# Remove (Middle)
# O(n)
arrayVar.remove('3')  # -> '3' => ['1', '2', '4', '5']

# Remove (Start)
# O(1)
arrayVar.popleft()  # -> '1' => ['2', '3', '4', '5']

# ---------------------------------------------------------------------------------------
# print(arrayVar)

print("\n**********************************************\n\n\n")
