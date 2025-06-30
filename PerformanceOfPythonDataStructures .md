# Lists
- Designed to optimize their implementation of a list so that the most common operation were very fast.
- It was also tried to make the less common operations fast, but when a tradeoff had to be made the performance of a less common operation was often sacrificed in favor of the more common operation.
- Two common operations are indexing and assigning to an index position. Both of these operations take the same amount of time no matter how large the list becomes.
- Both of these operations runs in O(1) time.
- Appending to a list runs in O(1) while the concatenation operator is O(n).
- Let us look at four different ways we might generate a list of n numbers.
``` python
def test1():
  l = []
  for i in range(1000):
    l = l + [i]
```

``` python
def test2():
  l = []
  for i in range(1000):
    l.append(i)
```

``` python
def test3():
  l = [i for i in range(1000)]
```

``` python
def test4():
  l = list(range(1000))
```
- Judging by the functions desinged and doing a time complexity analysis
    - The first function clearly performs concatenation thus it runs in O(n) = O(1000) in this case.
    - The second function performs the operation of append, thus it runs in O(1)
    - The third function and fourth is list comprehension and range , thus approx runs in < O(1)

- Another method to compute and analyse the time taken by each of these functions is to use `timeit`.
- We can create a `Timer` object whose parameters are two Python Statements.
- The first parameter is a Python statement that you want to time; the second parameter is a statement that will run once to set up the test.
- YOU CAN SEE THE CODE BELOW TO UNDERSTAND THE IMPLEMENTATION
``` python
import timeit
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print(f"Concatenation - {t1.timeit(number = 10000) } millisecond")

t2 = Timer("test2()", "from __main__ import test2")
print(f"Concatenation - {t2.timeit(number = 10000) } millisecond")

t3 = Timer("test3()", "from __main__ import test3")
print(f"Concatenation - {t3.timeit(number = 10000) } millisecond")

t4 = Timer("test4()", "from __main__ import test4")
print(f"Concatenation - {t4.timeit(number = 10000) } millisecond")
```

- It is interesting to note that the list comprehension is twice as fast as a `for` loop with an `append` operation.
-  In this case the statement `from __main__ import test1` imports the function `test1` from the `__main__` namespace into the namespace that timeit sets up for the timing experiment.
-  The `timeit` module does this because it wants to run the timing tests in an environment that is uncluttered by any stray variables you may have created, that may interfere with your function’s performance in some unforeseen way.

- The `pop` has two different times , it runs in O(1) when called on the end of the list, and runs in O(n) if called in the beginning of the list, or anywhere in the middle of the list.
-  The reason for this lies in how Python chooses to implement lists.
-  When an item is taken from the front of the list, in Python’s implementation, all the other elements in the list are shifted one position closer to the beginning.
-  This may seem silly to you now, but if you look this implementation also allows the index operation to be O(1).
-  This is a tradeoff that the Python implementors thought was a good one.

<hr/>

# Dictionaries
-  The second major Python data structure is the dictionary. As you probably recall, dictionaries differ from lists in that you can access items in a dictionary by a key rather than a position.
-  The thing that is most important to notice right now is that the get item and set item operations on a dictionary are O(1).
-  Another important dictionary operation is the contains operation. Checking to see whether a key is in the dictionary or not is also O(1).
- However we must not ignore the possibility of get items and set items operations to degenrate to O(n) performance but we will discuss that later.
- For now, the Big-O Performance metrics below assumes an average performance.
<ul>
  <li> **Operation**      **Time**</li>
</ul>
