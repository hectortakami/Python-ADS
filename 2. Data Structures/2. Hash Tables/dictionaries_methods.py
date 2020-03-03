
print("\n\n\n*************** HASH TABLES METHODS ***************\n")


def playHonk():
    return('Honk Honk!')


myDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1968,
    "honk": playHonk()
}

# ---------------------------------------------------------------------------------------

# Lookup | Access
# O(1)
value = myDictionary.get('brand')
# Can also be accessed by myDictionary['brand']

# To retreive all the keys inside the dictionary
dictKeys = myDictionary.keys()
# ['brand', 'model', 'year', 'honk']

# To retreive all the values inside the dictionary
dictValues = myDictionary.values()
# ['Ford', 'Mustang', 1968, 'Honk Honk!']

# Retreive both keys and values
dictKeysAndValues = myDictionary.items()
# [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1968), ('honk', 'Honk Honk!')]

# ---------------------------------------------------------------------------------------

# Insertion
# O(1)
myDictionary['year'] = 1987  # Change an existing key value
myDictionary['color'] = 'red'  # Creating another [key: value] property

# ---------------------------------------------------------------------------------------

# Remove
# O(1)
# Removes the item with the specified key name
myDictionary.pop('year')
# Can also be deleted by => del myDictionary['year']
# but the keyword 'del' is dangerous because it can also delete the entire dictionary
# in case of necessity in clear myDictionary we must use myDictionary.clear() => {}

# Removes the last inserted item (in this case ['color':'red'])
myDictionary.popitem()

# ---------------------------------------------------------------------------------------

# Miscellaneous Functions

# Verify if a key exists in the dictionary
if 'model' in myDictionary:
    print(' myDictionary have \'model\' as one of the keys in the dictionary')
    print(' => ' + str(myDictionary))

# Create a dictionary from given array of values as keys
keys = ['key1', 'key2', 'key3']
defaultValue = 'defaultValue'  # OPTIONAL can be only dict.fromkeys(keys)
thisDictionary = dict.fromkeys(keys, defaultValue)
# => {'key1': 'defaultValue', 'key2': 'defaultValue', 'key3': 'defaultValue'}

print("\n\n\n***************************************************\n")
