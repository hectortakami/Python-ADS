import collections
from typing import Counter, Deque, List;
import re;
from itertools import chain;
#import numpy as np;

# Big O = Upper Bound (Worst case)
# Big Omega (Q) = Lower Bound (Best case)
# Big Theta = Tight Bound (Best and Worst case are equal)

# Big O = Upper Bound (Worst case)
# Big Omega (Q) = Lower Bound (Best case)
# Big Theta = Tight Bound (Best and Worst case are equal)

''' 
Amortized time: If an ArrayList gets out-of-space it doubles (2X) it size so the insertion won't take O(1)
                Although, this happens once in a while so it worths the extra time allocating space
                for special edge cases. 
                - TL;DR: Worst case happens every once in a while. But once it happens, it won't happen 
                         again for so long.
'''

# O(2^n) = Recursive
# O(log n) = Divide & Conquer
# O(N*M) = Nested loop (1st list length N and second M)
# O(N+M) = Two loops one executing after another
# O(N^2) = Iterating through the same size list in a nested manner

########################
# INTERVIEW QUESTIONS #
#######################
''' isUnique(word:str) -> bool
    v1 O(N) = Finding most common char to be repeated less than 1 time

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''
def isUnique(word:str):
    most_common_char_and_freq = Counter(word).most_common(n=1); #[('l',2)]
    char_freq = most_common_char_and_freq [0][1]; # [('l',2)] -> 2
    if char_freq > 1 :
        return False;
    return True;

# ---------------------------------------------------------------------------------- #

''' checkPermutationN(a:str, b:str) -> bool
    v1 O(N) = Comparing char frequency dictionaries
    v2 O(log N) = Using "sorted" to compare strings (Tim Sort Algorithm) Big O(n log n)

Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. ** NOTE: Asumming both strings are same length **
'''
def checkPermutation2(a:str, b:str):
    a_sorted = sorted(a); # sorted() implemented with Tim Sort algorithm O(n log n)
    b_sorted = sorted(b); # with 'n' being despicable as both strings are same length
    return a_sorted == b_sorted; # ['e', 's', 't', 't'] == ['e', 't', 't', 'w']

def checkPermutation1(a:str, b:str):
    str_a_freq = Counter(a);
    str_b_frq = Counter(b);
    return str_a_freq == str_b_frq; # {'a': 1, 'b': 1, 'c': 1, 'd': 1} == {'d': 1, 'a': 1, 'b': 1, 'c': 1}

# ---------------------------------------------------------------------------------- #

''' URLfy(plainStr: str) -> str
    v1 O(2^regex_size + phrase_size) = Use RegEx substitution to replace white spaces with the '%20' string
    v2 O(n) = Use "replace()" in-built method which is optimized to modify the matching sub-strings

Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. 
'''
def URLfy2(phrase: str):
    return phrase.strip().replace(' ', '%20');

def URLfy1(phrase: str):
    url = re.sub('\s', '%20', phrase.strip() ); # strip() removes leading and trailing spaces
    return url;

# ---------------------------------------------------------------------------------- #

''' palindromePermutation(word: str) -> bool
    v1 O(n) = Count odd occurrences, if its pair this can form a palindrome otherwise there will be extra chars

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
'''

def palindromePermutation(word: str):
    char_freq_dict = dict(Counter(word.strip()));   # Convert word to frequency dictionary
    odd_repeated_chars = 0;                         # Count the letters that repeats an odd number of times
    for char_freq in char_freq_dict.values():
        if char_freq % 2 == 1:                      # If odd, 
            odd_repeated_chars += 1;                # add to counter
    return odd_repeated_chars % 2 == 0;             # If the counter is even you can form a palindrome (enough letters), not otherwise.
    ''' ** NOTE *** Alternative to reduce code size using filter().
     chars_that_repeats_odd_times = list(filter( lambda elem: elem % 2 == 1, char_freq_dict.values()));
     return len(chars_that_repeats_odd_times) % 2 == 0; 
    '''

# ---------------------------------------------------------------------------------- #

''' oneAwayEdits(a:str, b:str) -> bool
    v1 O(n) = Convert the strings to sets and get the difference() between them, if greater than 1 its not 1 edit away.

There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. ** NOTE *** Assume there is no spaces considered and same length
'''

def oneAwayEdits(a:str, b:str):
    chars_that_differ = 0; 
    if len(a) >= len(b): 
        chars_that_differ = set(a).difference(set(b));  # Convert strings to Sets so the difference() method can be used
    else:
        chars_that_differ = set(b).difference(set(a));
    return len(chars_that_differ) <= 1;                 # Check if difference is minor or equals 1.

# ---------------------------------------------------------------------------------- #

''' stringComprehensionForAll(phrase:str) -> str
    v1 O(n) = Get all frequecies, interleave arrays as string (char,ocurrencies).

String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a5b1c5.
'''

def stringComprehensionForAll(phrase:str):
    char_counter_dict = dict(Counter(phrase));
    chars_to_str = ''.join(list(char_counter_dict.keys()));                             # Chars converted to string
    freqs_to_str = ''.join(list(map(lambda x: str(x), char_counter_dict.values())));    # Occurrencies (int) mapped to int and then to a whole string
    # zip() interleaves both lists strings -> [('a', '5'), ('b', '1'), ('c', '5')]  
    interleaved_strings_as_set_tuples = zip(chars_to_str, freqs_to_str);       
    # from itertools import chain
    # chain.from_iterable() combines zip() tuples to make them key+value -> a5b1c5
    compressed_string = ''.join(list(chain.from_iterable(interleaved_strings_as_set_tuples))); 
    return compressed_string;
# ---------------------------------------------------------------------------------- #

''' stringComprehensionOrdered(phrase:str) -> str
    v1 O(n) = Iterate using aux variables to keep the current letter and its frequency concatenating the result string

String Compression: Similar to previous excercise, but in this case get the occurrencies ordered. 
For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def stringComprehensionOrdered(word:str):
    compressed_string = '';
    last_seen_letter = word[0];           # Store first char as pivot for comparisons
    occurrencies_before_next_letter = 0;  # Keps count for occurencies
    for char in word:                     # Iterates through all the chars in word
        # When the char changes we count 1 occurency and change the pointer storing the last count
        if last_seen_letter != char:
            compressed_string += last_seen_letter + str(occurrencies_before_next_letter);
            last_seen_letter = char;
            occurrencies_before_next_letter = 1;
        # Otherwise we keep increasing our counter for the same letter
        else:
            occurrencies_before_next_letter += 1;
    # At the end we add the last letter and its frequency to the comprressed string to have all the count
    compressed_string += last_seen_letter + str(occurrencies_before_next_letter);
    # If the resulting string is smaller we return it otherwise returns the input string
    if len(compressed_string) <= len(word):
        return compressed_string;
    return word;
# ---------------------------------------------------------------------------------- #

''' rotateMatrix90degrees(matrix:List[List[int]]) -> List[List[int]]
    v1 O(N^2) = 
        1. Reverse matrix (row order) to get last rows first to get the desired order in a descently ↓
        2. Get the coords inverted (x,y) now should be (y,x) because we need to stay on the same VERTICAL AXIS
           and keep changing the row to gather the results
    v2 O(1) = Usin NumPy library the operations are made IN-PLACE (reusing the matrix), so this reduces the complexity 

Rotate Matrix: Given an image represented by an NxN matrix (same size), where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
                ↓  ↓  ↓
→ [1, 2, 3]    [7, 4, 1]
→ [4, 5, 6] -> [8, 5, 2]
→ [7, 8, 9]    [9, 6, 3]

[x5, x1, x9, 11]    [15, 13, x2, x5]
[x2, x4, x8, 10] -> [14, x3, x4, x1]
[13, x3, x6, x7]    [12, x6, x8, x9]
[15, 14, 12, 16]    [16, x7, 10, 11]
'''
def rotateMatrix90degreesv2(matrix:List[List[int]]):
    # import numpy as np (requires a vEnv and pip installations)
    np_matrix = np.array(matrix);
    # Is the same as using in-built function "np.rot90(np_matrix)"
    rot_matrix = np.fliplr(np.transpose(np_matrix));
    return rot_matrix;

def rotateMatrix90degreesv1(matrix:List[List[int]]):
    matrix = list(reversed(matrix)) # Reverse matrix and re-convert the iterable to list
    rot_matrix = [];    # Result matrix (list of lists) #  ↓  ↓  ↓
    for x, row in enumerate(matrix):                    # [7, 8, 9]
                                                        # [4, 5, 6]
                                                        # [1, 2, 3]
        rot_row = [];   # List to store the rotated values per row
        for y, _ in enumerate(row):   
            rot_row.append(matrix[y][x]);  
                                        # [7, 4, 1]
                                        # [8, 5, 2]
                                        # [9, 6, 3]
        rot_matrix.append(rot_row);
    return rot_matrix;
# ---------------------------------------------------------------------------------- #

''' zeroMatrix(matrix:List[List[int]]) -> List[List[int]]
    v1 O(2N) = We only care about the 1st "0" occurence found at the row and then we modify the matrix
    v2 O(2N^2) = The algorithm obtain all column indexes from original matrix and traverse 
                 the NEW matrix to modify the missing columns.

Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. 
'''
def zeroMatrixv1(matrix:List[List[int]]):
    # Only matches and handles one "0" coincidence per row.
    new_matrix = [];
    zero_idx = -1;
    for row in matrix:
        if 0 in row:
            zero_idx = row.index(0);
            row = [0]*len(row)  
        new_matrix.append(row);
    
    if zero_idx != -1:
        for row in matrix:
            row[zero_idx] = 0;
    return new_matrix;

def zeroMatrixv2(matrix:List[List[int]]):
    new_matrix = [];
    zero_idx = [];
    for row in matrix:
        if 0 in row:
            # Obtain all indexes from same occurence (in this case "0");
            zero_idx.extend([idx for idx, col in enumerate(row) if col == 0]) 
            row = [0]*len(row)  
        new_matrix.append(row);

    for row_idx, row_list in enumerate(new_matrix):
        if 0 not in row:
            for col_idx, _ in enumerate(row_list):
                if col_idx in zero_idx:
                    new_matrix[row_idx][col_idx] = 0;
        continue;
    return new_matrix;     
# ---------------------------------------------------------------------------------- #
      
''' stringRotation(str1: str, str2: str) -> bool
    v1 O(N) = Use deque from collections to pop the last char and add it at the beginning, then compare the result with the other
              string. If matches exists a possible string rotation.

Assume you have a method isSubs t rin g which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of si using only one
call to isSubs t rin g [e.g., "waterbottle" is a rotation of "erbottlewat").
'''
def stringRotation(str1: str, str2: str):
    # Edge cases (not matching lenght and same string)
    if len(str1) != len(str2):
        return False;
    if str1 == str2:
        return True;

    deque_str2 = Deque(str2);   # String deque de-construction to use appendleft()   
    rotations_until_circle_back = len(str2)-1;  # Possible rotation rounds removing the original string

    while rotations_until_circle_back > 0:
        last_char = deque_str2.pop();       # Remove last char
        deque_str2.appendleft(last_char);   # Add it to the start
        if str1 == ''.join(list(deque_str2)):
            print(rotations_until_circle_back);
            return True;
        rotations_until_circle_back -= 1;   # DONT FORGET TO DECRESE (infinite loop)
    return False;
# ---------------------------------------------------------------------------------- #

def main():
    # ----------------------------------------------------------------- #
    '''
    # stringRotation()
    print(stringRotation('erbottlewat','waterbottle'));     # Return: True
    '''
    # ----------------------------------------------------------------- #
    '''
    # zeroMatrix()
    print(zeroMatrixv2([[0,1,2,0],[3,4,5,2],[1,3,1,5]]));     # Result: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print(zeroMatrixv1([[1,1,1],[1,0,1],[1,1,1]]));           # Result: [[1,0,1],[0,0,0],[1,0,1]]
    '''
    # ----------------------------------------------------------------- #
    '''
    # rotateMatrix90degrees()
    print(rotateMatrix90degreesv1([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]));    # Result: [15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]
    print(rotateMatrix90degreesv1([[1,2,3],[4,5,6],[7,8,9]]));    # Result: [[7,4,1],[8,5,2],[9,6,3]]
    '''
    # ----------------------------------------------------------------- #
    '''
    # stringComprehensionOrdered()
    print(stringComprehensionOrdered('aabcccccaaa'));  # Result: 'a2blc5a3'
    '''
    # ----------------------------------------------------------------- #
    '''
    # stringComprehensionForAll()
    print(stringComprehensionForAll('aabcccccaaa'));  # Result: 'a5b1c5'
    '''
    # ----------------------------------------------------------------- #
    '''
    # oneAwayEdits()
    print(oneAwayEdits('pale', 'pie'));     # Result: False
    print(oneAwayEdits('pales', 'pale'));   # Result: True
    print(oneAwayEdits('pale', 'bale'));    # Result: True
    print(oneAwayEdits('pale', 'bake'));    # Result: False
    '''
    # ----------------------------------------------------------------- #
    '''
    # palindromePermutations()
    print(palindromePermutation('Tact Coa'));       # Result: True ({"taco cat", "atc o eta", etc..})
    print(palindromePermutation('geeksforgeeks'));  # Result: False (No palindrome possible)
    '''
    # ----------------------------------------------------------------- #
    '''
    # URLfy()
    print(URLfy1("Mr 3ohn Smith"));     # Result: "Mr%203ohn%20Smith"
    print(URLfy2("Mr John Smith   "));  # Result: "Mr%203ohn%20Smith"
    '''
    # ----------------------------------------------------------------- #
    '''
    # checkPermutation()
    print(checkPermutation1('abcd', 'dabc'));    # Result: True
    print(checkPermutation1('test', 'ttew'));    # Result: False
    print(checkPermutation2('abcd', 'dabc'));    # Result: True
    print(checkPermutation2('test', 'ttew'));    # Result: False
    '''
    # ----------------------------------------------------------------- #
    '''
    # isUnique()
    print(isUnique("Hello"));   # Result: False
    print(isUnique("Hector"));  # Result: True
    '''
    # ----------------------------------------------------------------- #
    return;
main();