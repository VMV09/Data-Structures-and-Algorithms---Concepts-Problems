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
