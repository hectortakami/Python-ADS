# https://evalutron3001.googleplex.com/categoryquestions?category=Short%20Coding

from collections import deque
from itertools import combinations, permutations
from operator import index
import random
import string
from typing import Counter

''' palindromePermutation(s:str)
    v1 O(n+n!) = Needs to analyze every substring finding a palindrome
    v2 O(n) = Count the char occurrences, if more than one char has an ODD number, no palindrome can be formed.

Given a String 's', return true if at-least one permutation of 's' can be palindromic.
For example: "abcbc" can have have cbabc as a palindromic permutation (so return true)
Whereas "abccc" can't have any palindromic permutation (so return false)
'''
def palindromePermutationV1(s:str):
    can_have_palindrome_permutation = False;
    length = len(s) + 1
    # Permutations cost O(N!)
    substrings = permutations(s);
    for sub in substrings:  # O(N)
        if list(sub) == list(reversed(sub)):
            can_have_palindrome_permutation = True;
            break;
    print(can_have_palindrome_permutation);
    return can_have_palindrome_permutation;
    
def palindromePermutationV2(s:str):
    char_count = Counter(s);
    odd_chars = 0;
    for char in list(char_count.keys()):
       if char_count[char] % 2 == 1:
           odd_chars += 1;
    can_have_palindrome_permutation = odd_chars <= 1;
    print(can_have_palindrome_permutation);
    return  can_have_palindrome_permutation;

#palindromePermutationV2('abcbc');
#palindromePermutationV2('abccc');

# ------------------------------------------------------------- #

'''
Find the top 2 IP addresses from a web server log file.

||  RECOMMENDATION
||  Candidate should identify the need for a hashmap. Then it's a 
||  matter of sorting by the values and returning the top 10.
'''

def findTopIPs(file_log:str):
    ip_list = [];
    for line in file_log.strip().split('\n'):
        ip = line.split(',')[3];
        ip_list.append(ip);
    top_ten_IPs = list(Counter(ip_list).most_common(2));
    print(top_ten_IPs);    
    return;

sampleLog = '''
14716104719,GET,/index.html,10.10.10.1
14716104719,GET,/index.html,10.10.10.1
14716104719,GET,/index.html,127.10.24.1
14716104719,GET,/index.html,10.10.10.1
14716104719,GET,/index.html,239.19.5.1
14716104719,GET,/index.html,239.19.5.1
14716104719,GET,/index.html,10.10.10.1
'''
# findTopIPs(sampleLog);

# ------------------------------------------------------------- #

'''
Describe good algorithm to find the word frequency in a document. Analyze the space/time 
complexity of your algorithm. All non-letter characters are treated as space characters.

||  RECOMMENDATION
||  Great candidates should ask about the language of the document and the file format.
||  Great candidates can also mention that this is embarrassingly parallel.
'''

def wordFrequency(text:str):
    txt = text.strip();
    words = txt.split(' ');
    word_frequency = Counter(words);
    print(word_frequency);
    return;

sampleText = "\n Apple Mango Orange Mango Guava Guava Mango\n "
# wordFrequency(sampleText);

# ------------------------------------------------------------- #

'''
Implement a function to convert change into the coins required using the smallest number of coins.
There are unlimited coins available and the list of values is given:
coins = [50, 20, 10, 5, 2, 1]
'''

def getChange(amount:int):
    coins = [50, 20, 10, 5, 2, 1];
    change = {}
    for coin in coins:
        if amount // coin != 0:
            change[coin] = amount // coin;
            amount -= (coin * change[coin]);     
    print(change);     
    return;

# getChange(71);
# getChange(50);
# getChange(105);

# ------------------------------------------------------------- #

'''
Given an array of integers, return all pairs of integers whose difference is a given number.

- Brute force: O(n^2) [disqualified] TC walks through each combination of elements in the array.
- O(n log n) [leaning no hire] TC sorts the array. TC iterates through 2 poiunters in the array while their delta is &amp;lt; P.
- O(n) [hire] TC stuffs the array into an unordered map or unordered set to utilize the O(1) lookup time.

Then, for each element in the array, TC sees if ( [el] + P ) exists in the unordered set.

||  RECOMMENDATION
||  If TC leverages unordered_set over unordered_map
||  if TC can distinguish the data structure utilized for unordered_set (hash map) vs set()
'''

def findDifferenceComplement(arr: list, diff: int):
    for x in arr:
        if (x + diff) in arr:
            complement_pair = (x, arr[arr.index(x + diff)]);
            print(complement_pair);
            return complement_pair;

# findDifferenceComplement([2,4,6,7,9], 3);
            
# ------------------------------------------------------------- #

'''
You a have a file with the following records:

product_id, retailer_id
1, 100
2, 200
3, 300
4, 100
1, 200
2, 300

Write a function that accepts a retailer_id and returns the list of product_ids that only that retailer has.
'''

def processRetailer(file:str, retailer:int):
    file = file.strip();
    retailer_dict = {};
    for line in file.split('\n')[1::]:
        data = line.split(',');
        product_id = data[0].strip();
        retailer_id = int(data[1].strip());
        if retailer_id in retailer_dict:
            retailer_dict[retailer_id].append(product_id);
        else:
            retailer_dict[retailer_id] = [product_id];          
    print(retailer_dict[retailer]);
    return;

sampleFile = '''
product_id, retailer_id
1, 100
2, 200
3, 300
4, 100
1, 200
2, 300
'''
# processRetailer(sampleFile, 100);
# processRetailer(sampleFile, 200);
# processRetailer(sampleFile, 300);

# ------------------------------------------------------------- #

'''
Write a function that determines if one string is an anagram of another.
ANAGRAM: A word formed with the same letters in different order.
'''

def isAnagram(str1:str, str2:str):
    str1_char_count = Counter(str1);
    str2_char_count = Counter(str2);
    return str1_char_count == str2_char_count;

# print(isAnagram('fried', 'fired'));
# print(isAnagram('listen', 'silent'));
# print(isAnagram('dog', 'cat'));

# ------------------------------------------------------------- #

'''
A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

AKA: Write a function that prints the content of a binary tree, in any order.   
'''

class Node:
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;
    
def preOrderTraversal(root: Node, nodes: list = []):
    if not root:
        return;
    nodes.append(root.data);
    if root.left is not None:
        preOrderTraversal(root.left, nodes);
    if root.right is not None:
        preOrderTraversal(root.right, nodes);
    return nodes; # Node list can grow log2(n) which is the amount of levels in the tree
    
def inOrderTraversal(root: Node, nodes: list = []):
    if not root:
        return;
    if root.left is not None:
        inOrderTraversal(root.left, nodes);
    nodes.append(root.data);
    if root.right is not None:
        inOrderTraversal(root.right, nodes);
    return nodes; # Node list can grow log2(n) which is the amount of levels in the tree

def postOrderTraversal(root: Node, nodes: list = []):
    if not root:
        return;
    if root.left is not None:
        postOrderTraversal(root.left);
    if root.right is not None:
        postOrderTraversal(root.right);
    nodes.append(root.data);
    return nodes;   # Node list can grow log2(n) which is the amount of levels in the tree

def levelOrderTraversal(root: Node):
    levels = []     
    queue = deque([]);  # Queue can grow up to 2^n (max amount of nodes per level)
    queue.append(root);
    while bool(queue):
        current = queue.popleft();
        if current.left is not None:
            queue.append(current.left);
        if current.right is not None:
            queue.append(current.right);
        levels.append(current.data);            
    return levels;

root = Node('A');
root.left = Node('B');
root.right = Node('C');
root.left.left = Node('D');
root.left.right = Node('E');
root.right.left = Node('F');
#                                      A
#                                  B       C
#                               D     E  F
# ====== Depth First Search Traversal ======
# print(preOrderTraversal(root));     # ['A', 'B', 'D', 'E', 'C', 'F'] 
# print(inOrderTraversal(root));      # ['D', 'B', 'E', 'A', 'F', 'C']
# print(postOrderTraversal(root));    # ['D', 'E', 'B', 'F', 'C', 'A']
# ====== Breadth First Search  ======

# print(levelOrderTraversal(root));   # ['A', 'B', 'C', 'D', 'E', 'F']

# ------------------------------------------------------------- #

'''
You have an array with unique items e.g [4, 2, 3, 1, 5, 6]

Write a function drag that takes two parameters, startIndex and endIndex and moves the item at the start index to the end index.
e.g function (3, 0) -> [ 1, 4, 2, 3, 5, 6]
'''

def dragItem(arr: list, start: int, end: int):
    element = arr.pop(start);
    arr.insert(end, element);   # O(N)
    return arr;

# print(dragItem([4, 2, 3, 1, 5, 6], 3, 0));  # [1, 4, 2, 3, 5, 6]

# ------------------------------------------------------------- #

'''
Given an unordered list of three integers, write a function to check if they can form a valid date.
E.g. (2000, 14, 3) => valid.
(2000, 3, 2000) => invalid.

NOTE: The order should be YEAR/DAY/MONTH and assuming the list will cointain the values ordered.
- Also is not considering LEAP YEARS (February with +1 days, this happens every 4 years) 
'''

def isValidDate(vals: list):
    is_year_suitable = vals[0] // 1000 != 0;
    is_day_suitable = vals[1] > 0 and vals[1] <= 31;
    is_month_suitable = vals[2] > 0 and vals[2] <= 12;
    return is_day_suitable and is_month_suitable and  is_year_suitable;

# print(isValidDate([2000, 14, 3]));
# print(isValidDate([2000, 3, 2000]));

# ------------------------------------------------------------- #

'''
Determine values not shared between two lists. Given a list A and B, returns a 
list of elements in A but not B and another list of elements in B but not A.


For example, given these two lists:
A = [1, 4, 10, 10, 5, 10]
B = [5, 3, 4, 4]

The outputs should be:
A not B = [1, 10]
B not A = [3]
'''

def differenceBetweenLists(a: list, b:list):
    a_with_no_duplicates = set(dict.fromkeys(a));
    b_with_no_duplicates = set(dict.fromkeys(b));
    difference = a_with_no_duplicates.difference(b_with_no_duplicates);
    print(list(difference));
    return difference;

A = [1, 4, 10, 10, 5, 10];
B = [5, 3, 4, 4];
# differenceBetweenLists(A, B);   # [1, 10]
# differenceBetweenLists(B, A);   # [3]

# ------------------------------------------------------------- #

'''
Calculate slowest method from a log file of method calls, start, and end times. Assuming that a given method can be executed by just one user at a given point in time, and assume that the log lines are well formed.

Example log:
Method1 start 1500000000100
Method1 end 1500000000201
Method2 start 1500000001100
Method1 start 1500000001101
Method2 end 1500000001222
Method3 start 1500000001572
Method3 end 1500000003629
Method1 end 1500000007629

Example Output:
Method1


Note: Assume all processes have eventually a starting and an ending point;
'''

def calculateMethodLatencies(file: str):
    methods = {};
    slower_method = ('',0);
    lines = file.strip().split('\n');
    for line in lines:
        data = line.split(' ');
        method_name = data[0];
        time = int(data[2]);
        if method_name in methods:
            methods[method_name]['times'].append(time);
        else:
            methods[method_name] = {'times':[], 'deltas':[], 'greater_delta':None}
            methods[method_name]['times'].append(time);

        method_time_list = methods[method_name]['times'];
        if len(method_time_list) % 2 == 0:
            end = method_time_list[len(method_time_list)-1];
            start = method_time_list[len(method_time_list)-2];
            delta = end - start;
            methods[method_name]['deltas'].append(delta);
            if  methods[method_name]['greater_delta'] is None or \
                (delta) > methods[method_name]['greater_delta']:
                methods[method_name]['greater_delta'] = delta;
                if slower_method is ('',0) or (delta) > slower_method[1]:
                    slower_method = (method_name, delta);
    
    print(slower_method);
    return slower_method;

sampleFile = '''
Method1 start 1500000000100
Method1 end 1500000000201
Method2 start 1500000001100
Method1 start 1500000001101
Method2 end 1500000001222
Method3 start 1500000001572
Method3 end 1500000003629
Method1 end 1500000007629
'''
# calculateMethodLatencies(sampleFile);   # ('Method1', 6528)

# ------------------------------------------------------------- #

'''
Write 2 function that interacts with a 2D integer array (matrix)

1. Write an update function which accepts (x, y, value) to update the array.
2. Write a query function which accepts (x1, y1) (x2, y2) and returns the sum of all numbers within the rectangle.
'''

def updateMatrixElement(matrix: list, x: int, y: int, value: int):
    if x >= len(matrix) or y >= len(matrix[0]):
        return;
    matrix[x][y] = value;
    return matrix;

def sumOfTwoMatrixElements(matrix: list, x1: int, y1: int, x2: int, y2: int):
    if x1 >= len(matrix) or y1 >= len(matrix[0]) or x2 >= len(matrix) or y2 >= len(matrix[0]):
        return;
    x1y1 = matrix[x1][y1];
    x2y2 = matrix[x2][y2];
    return x1y1 + x2y2;

matrix = [
    [ 2, 3, 5, 6, 8, 9, 1 ],    #     [ 2, 3, 5, 6, 8, 9, 1   ],
    [ 1, 4, 6, 3, 7, 2, 0 ],    #     [ *1, 4, 6, 3, 7, 2, 0  ],
    [ 1, 3, 5, 7, 9, 2, 4 ],    #     [ 1, 3, 5, 7, 9, 2, 4   ],
    [ 5, 7, 9, 1, 3, 5, 8 ],    #     [ 5, 7, 9, *999, 3, 5, 8],
    [ 0, 9, 8, 1, 3, 6, 7 ],    #     [ 0, 9, 8, 1, 3, 6, 7   ],
    [ 4, 6, 1, 8, 0, 2, 1 ],    #     [ 4, 6, 1, 8, 0, 2, 1   ],
];

# updateMatrixElement(matrix, 3, 3, 999);
# print(sumOfTwoMatrixElements(matrix, 3, 3, 1, 0))   # 1000;

# ------------------------------------------------------------- #

'''
Write a function that receives a string as an input and outputs 
the longest sequence of consecutive characters.
Examples:
Input: Gooogle Output: ooo
Input: Googleee Output: eee
'''

def longestConsecutiveLetters(word: str):
    word = word.lower();
    longest_consecutive_letter = ('',0);

    last_seen_letter = None;
    last_seen_count = 0;
    for letter in word:
        if last_seen_letter is None:
            last_seen_letter = letter;
            last_seen_count = 1;
        else:
            if last_seen_letter == letter:
                last_seen_count += 1;
                if longest_consecutive_letter == ('',0) or \
                    last_seen_count > longest_consecutive_letter[1]:
                    longest_consecutive_letter = (letter,last_seen_count);
            else:
                last_seen_letter = letter;
                last_seen_count = 1;            
    letter_repeated = longest_consecutive_letter[0]*longest_consecutive_letter[1];
    return letter_repeated;

# print(longestConsecutiveLetters('Gooogle'));
# print(longestConsecutiveLetters('Googleee'));

# ------------------------------------------------------------- #

'''
Write a function to merge 2 arrays?

Follow up:
Write a function to merge 2 arrays in sorted order?
Write a function to merge 2 arrays in sorted order without duplicates?
Write a function to merge 2 arrays picking items at intervals.
Write a function to merge N arrays?

NOTE: The extend() function modifies the original list in-place meaning that any
      consecutive reference to it will be returned with the extended value.
'''

def mergeArrays(lst1: list, lst2: list):
    merge1 = lst1;
    merge1.extend(lst2)
    return merge1;

def mergeArraysSorted(lst1: list, lst2: list):
    merge2 = lst1;
    merge2.extend(lst2)
    return sorted(merge2);

def mergeArraysSortedNoDuplicates(lst1: list, lst2: list):
    merge3 = lst1;
    merge3.extend(lst2)
    return list(dict.fromkeys(merge3));

def mergeArraysAtInterval(lst1: list, lst2: list, interval: int):
    merge4 = [];
    for idx in range(0, len(lst1), interval):
        merge4.append(lst1[idx]);
        merge4.append(lst2[idx]);
    return merge4;

A = [6,9,3,5,1]
B = [3,9,2,2,4]

#print(mergeArrays(A,B));
#print(mergeArraysSorted(A,B));
#print(mergeArraysSortedNoDuplicates(A,B));
#print(mergeArraysAtInterval(A, B, 2));

# ------------------------------------------------------------- #

'''
Write a function to identify the first unique character in a string.
'''

def firstUniqueChar(word: str):
    word = word.lower();
    for idx, letter in enumerate(word):
        prev_letters = word[:idx];
        next_letters = word[idx+1:];
        if letter not in prev_letters and letter not in next_letters:
            return letter;
    return -1;

# print(firstUniqueChar('Google'));      # 'l'
# print(firstUniqueChar('Seahawks'));    # 'e'
# print(firstUniqueChar('Seattle'));     # 's'

# ------------------------------------------------------------- #

'''
Write a function that accepts a number encoded as an array of 
digits, e.g. [1,9,3,8] for the number 1938, and returns the encoded 
number incremented by 1, e.g. returns [1,9,3,9].
'''

def encodedAdittion(digits: list):
    number = int(''.join(map( lambda x: str(x) , digits)));
    number = number + 1;
    return list(map( lambda x : int(x) , list(str(number))));

def encodedAdditionNotCasting(digits: list):
    idx = len(digits)-1     # last digit (units)
    digits[idx] += 1;       # add +1

    is_carrying_one = False;    # keeps track about the +1 to the next unit group
    for _ in reversed(digits):
        if is_carrying_one:     
            digits[idx] += 1;             # if enabled, add 1 to the 
            is_carrying_one = False;      # next units and turn off the flag
        if digits[idx] == 10:
            digits[idx] = 0;              # if units are 10, change it to '0'
            is_carrying_one = True;       # and let the next units know we need to add 1  
        idx-=1;     # decrement the counter (remember we are traversing the list backwards). 
    return digits;
    

# print(encodedAdittion([1,9,3,9]));
# print(encodedAdditionNotCasting([1,9,9,9]));

# ------------------------------------------------------------- #

'''
Write a function or method any language that will accept an 
integer array and identify the first sequence of increasing Integers.

Follow-up: enhance the code so that it will count the number of 
increasing sequences of integers in the array.
'''

def firstIncreasingSequence(data: list):
    last_value_seen = data[0];          # took the 1st element on list to compare with
    first_increasing_sequence = [];     # stores the increasing sequence found
    is_sequence_started = False;        # flag to know if the sequence was started

    # condition block to validate if the 1st element is smaller than the next one
    # meaining the sequence is increasing
    if last_value_seen < data[1]:
        first_increasing_sequence.append(last_value_seen);
        is_sequence_started = True;

    for idx in range(1,len(data)):
        # stop condition that checks if an increasing sequence is sttoped 
        # because the current value is not bigger than the previous one
        if is_sequence_started and data[idx] < last_value_seen:
            return first_increasing_sequence;
        # if the current value is bigger than the previous the sequence starts 
        # and we add the value to the list. Also enableing the flag.
        if data[idx] > last_value_seen:
            first_increasing_sequence.append(data[idx]);
            is_sequence_started = True;
        # continue with the next item
        last_value_seen = data[idx];
    return first_increasing_sequence;

def countIncreasingSequences(data: list):
    last_value_seen = data[0];          
    current_sequence = [];     
    list_of_increasing_sequences = [];     
    is_sequence_started = False;        

    if last_value_seen < data[1]:
        current_sequence.append(last_value_seen);
        is_sequence_started = True;

    for idx in range(1,len(data)):
       
        if is_sequence_started and data[idx] < last_value_seen:
            # the main difference with the previous code is that now we 
            # store all sequences in a list and reset the flags to continue
            # iterating through the values.
            list_of_increasing_sequences.append(current_sequence);
            is_sequence_started = False;
            current_sequence = [];
        
        if data[idx] > last_value_seen:
            current_sequence.append(data[idx]);
            is_sequence_started = True;
     
        last_value_seen = data[idx];
    # retreive the list of increasing sequences
    return list_of_increasing_sequences;

#print(firstIncreasingSequence([2,1,7,8,9,4,3]));      # [7,8,9]
#print(firstIncreasingSequence([1,2,3,6,5,4]));        # [1,2,3,6]
#print(firstIncreasingSequence([4,3,2,1]));            # []
#print(countIncreasingSequences([2,3,1,7,8,9,4,3]));   # [2,3] [7,8,9]

# ------------------------------------------------------------- #

'''
We need a program that will count the number of occurrences of certain words in a matrix.

Write a function in the language of your choice that accepts two parameters. 
The first parameter is a 2-dimensional array of characters, and the second parameter 
is an array of strings.

An example would be the following inputs:

A B X D W H O W
W O R D S E U W
O R H W O R D S
R S E I J E E S
D E R G H I R K
S I E P R S E U

['WORDS', 'HERE']

This should return 5 (3 instances of WORDS, and 2 instances of HERE).

ASSUMPTION: No words inverted or reversed (not in x or y direction) and no words in diagonal either.
'''

# function that retrieves easily an entire column of a matrix 
def _column(matrix, idx):
    return [row[idx] for row in matrix];

def findInCrossword(crossword: list, words: list):
    words_dict = dict.fromkeys(words);  # create a dict to keep track of the word coincidence count
    rows = [];  # all rows converted to string each
    cols = [];  # all cols converted to string each
    # iterate through rows and convert them to string to store them in rows[] list
    for row in crossword:
        row_collapsed = ''.join(row);
        rows.append(row_collapsed);
    # iterate through columns and convert them to string to store them in cols[] list
    for col_idx in range(0,len(crossword[0])):
        col = _column(crossword, col_idx);
        col_collapsed = ''.join(col);
        cols.append(col_collapsed);
    # review each word
    for word in words:
        # find the rows & cols (converted to string) that contains the word we are looking for
        rows_containing_word = list(filter( lambda row: word in row , rows));
        cols_containing_word = list(filter( lambda col: word in col , cols));
        # update the total of coincidences found per each word
        words_dict[word] = len(rows_containing_word) + len(cols_containing_word);
    print(words_dict);
    return words_dict;

crossword = [
    ['A', 'B', 'X', 'D', 'W', 'H', 'O', 'W' ],
    ['W', 'O', 'R', 'D', 'S', 'E', 'U', 'W' ],
    ['O', 'R', 'H', 'W', 'O', 'R', 'D', 'S' ],
    ['R', 'S', 'E', 'I', 'J', 'E', 'E', 'S' ],
    ['D', 'E', 'R', 'G', 'H', 'I', 'R', 'K' ],
    ['S', 'I', 'E', 'P', 'R', 'S', 'E', 'U' ],
]
#findInCrossword(crossword, ['WORDS', 'HERE']);

# ------------------------------------------------------------- #

'''
Shuffle an array in a uniform way.

Note: A uniform shuffle of a table 𝑎=[𝑎0,...,𝑎𝑛−1] is a random permutation of its 
elements that makes every rearrangement equally probable. 

- The key here is to generate a RANDOM index to SWAP elements within the list's range (0 <-> list size)
- This makes the probability of swapping 1/list_length or 1/n equaly for all the elements.
'''

def shuffleUniform(arr: list):
    size = len(arr);
    for i in range(0, size):
        j = random.randint(i, size-1);
        (arr[i], arr[j]) = (arr[j], arr[i]);
    print(arr);
    return arr;

# shuffleUniform([1,2,3,4,5,6]);

# ------------------------------------------------------------- #

'''
In a worksheet application, like in Excel or Google Sheets, columns are labeled 
from "A"-"Z" for the first 26 columns, then "AA" for the 27th, all the way through 
"AZ" and then "ZZ", followed by "AAA".  Write a function that will take in an 
integer and return the correct label for that column.

f(1)="A"
f(27)="AA"
f(18278)="ZZZ"

'''

def excel_column_name(num : int):
    alphabet = string.ascii_uppercase;
    column = '';
    while num > 0:                  # Evaluate if number given can still be divisable /26
        letter_idx = num % 26;      # Get the modulus to obtain the letter index on the alphabet

        # EDGE CASE, if modulus is divisable /26 (or multiple of 26)
        # that means we reach the end of an alphabet and we ad the letter 'Z'
        # then we divide the result DECREMENTING -1 because the alphabet array
        # contains only indexes from [0-25] 
        if letter_idx == 0:
            column += 'Z';
            num = (num//26)-1;
        else:
            # if the modulus is greater than '0' we only find the index_value -1
            #  in the alphabet list, add it to the resulting word and divide /26 again
            column += alphabet[letter_idx - 1];
            num //= 26;

    # We return the resulting word reversed (appends '+=' add every new char at the end)
    return column[::-1];    

def excel_column_number(column : str):
    alphabet = string.ascii_uppercase;

    num = 0;    # keeps track about the columns counted
    for letter in column:   # iterates through ach given letter in order
        letter_index = alphabet.index(letter) + 1;  # finds the letter index in the alphabet list and adds 1 to it
        # first we multiply the previous sum number to the entire
        # alphabet length that means:
        # - 1st loop 26*0 = 0, 
        # - 2nd loop 26*letter = total amount of completed columns until next set AX = 26*1, BX = 26*2, CX = 26*3... 
        num *= 26;
        # then we add the letter value to the number
        num += letter_index;

    return num;

# print(excel_column_name(1));        # A
# print(excel_column_name(27));       # AA
# print(excel_column_name(18278));    # ZZZ

# print(excel_column_number('A'));      # 1
# print(excel_column_number('AA'));     # 27
# print(excel_column_number('ZZZ'));    # 18278

# ------------------------------------------------------------- #

'''
Write a function, program that accepts a filled out suduku board and then checks if the board is a valid solution.
- Each row must have the numbers 1-9
- Each column must have the numbers 1-9
- Each 3x3 box must have the numbers 1-9

7 9 2 | 1 5 4 | 3 8 6
6 4 3 | 8 2 7 | 1 5 9
8 5 1 | 3 9 6 | 7 2 4
---------------------
2 6 5 | 9 7 3 | 8 4 1
4 8 9 | 5 6 1 | 2 7 3
3 1 7 | 4 8 2 | 9 6 5
---------------------
1 3 6 | 7 4 8 | 5 9 2
9 7 4 | 2 1 5 | 6 3 8
5 2 8 | 6 3 9 | 4 1 7
'''
# function that retrieves easily an entire column of a matrix 
def _column(matrix, idx):
    return [row[idx] for row in matrix];

def isSudokuValid(sudoku: list):
    
    # The solution is simple, we do NOT CARE about the 3x3 sub-matrixes
    # If all columns and all matrixes contain 1 time all sudoku numbers
    # from (1-9) we can say the solution is correct, otherwise return False
    correct_solution = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1};

    for col_idx in range(0, len(sudoku[0])):
        column = _column(sudoku, col_idx);
        sudoku_column_counter = Counter(column);
        if sudoku_column_counter != correct_solution:
            return False;

        # Also works comparing all values through an IF condition including them
        # if 1 not in column or 2 not in column or 3 not in column or \
        #     4 not in column or 5 not in column or 6 not in column or \
        #         7 not in column or 8 not in column or 9 not in column:
        #         return False;

    for row in sudoku:
        sudoku_row_counter = Counter(row);
        if sudoku_row_counter != correct_solution:
            return False;
    
    return True;

sudoku1 = [
    [7, 9, 2, 1, 5, 4, 3, 8, 6], 
    [6, 4, 3, 8, 2, 7, 1, 5, 9],
    [8, 5, 1, 3, 9, 6, 7, 2, 4],
    [2, 6, 5, 9, 7, 3, 8, 4, 1],
    [4, 8, 9, 5, 6, 1, 2, 7, 3],
    [3, 1, 7, 4, 8, 2, 9, 6, 5],
    [1, 3, 6, 7, 4, 8, 5, 9, 2],
    [9, 7, 4, 2, 1, 5, 6, 3, 8],
    [5, 2, 8, 6, 3, 9, 4, 1, 7],
];
sudoku2 = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5], 
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
];

# print(isSudokuValid(sudoku1));  # True
# print(isSudokuValid(sudoku2));  # False

# ------------------------------------------------------------- #

'''
Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) 
to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one 
instance of the digits from 1 to 9. 

https://www.askpython.com/python/examples/sudoku-solver-in-python
'''

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
        

    

sudoku = [
    [3, 0, 6,  5, 0, 8,  4, 0, 0],    #  3 1 6 | 5 7 8 | 4 9 2
    [5, 2, 0,  0, 0, 0,  0, 0, 0],    #  5 2 9 | 1 3 4 | 7 6 8
    [0, 8, 7,  0, 0, 0,  0, 3, 1],    #  4 8 7 | 6 2 9 | 5 3 1
                                      #  ---------------------
    [0, 0, 3,  0, 1, 0,  0, 8, 0],    #  2 6 3 | 4 1 5 | 9 8 7
    [9, 0, 0,  8, 6, 3,  0, 0, 5],    #  9 7 4 | 8 6 3 | 1 2 5
    [0, 5, 0,  0, 9, 0,  6, 0, 0],    #  8 5 1 | 7 9 2 | 6 4 3
                                      #  ---------------------
    [1, 3, 0,  0, 0, 0,  2, 5, 0],    #  1 3 8 | 9 4 7 | 2 5 6
    [0, 0, 0,  0, 0, 0,  0, 7, 4],    #  6 9 2 | 3 5 1 | 8 7 4
    [0, 0, 5,  2, 0, 6,  3, 0, 0],    #  7 4 5 | 2 8 6 | 3 1 9 
]

if (Suduko(sudoku, 0, 0)):
    puzzle(sudoku)
else:
    print("Solution does not exist:(")
