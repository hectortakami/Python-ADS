##### Get all combinations

```py
from itertools import combinations
# ...
s = 'abc'
res = [s[x:y] for x, y in combinations(
       range(len(s) + 1), r = 2)]
print(res);
```

`'a', 'ab', 'abc', 'b', 'bc', 'c'`

##### Get all permutations

_same size, same letters, different order_

```py
from itertools import permutations
# ...
s = 'abc'
res = list(permutations(s));
```

`('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')`

# TODO map(), filter(), reduce()

# TODO read & write files

##### Remove duplicates from list

```py
myList = [1, 4, 10, 10, 5, 10];
myList_no_duplicates = list(dict.fromKeys(myList));
```

`[1, 4, 10, 5]`
