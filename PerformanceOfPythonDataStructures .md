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
