# Lists in Python
## Methods to Construct a List
- The Code Snippets below demonstrates the different methods to initilaise and construct a list.
- List is a Data Structure that can store multiple data type data in them.
- The below suggests the `Square Brackets` method to initialise the list.
```python
a = [1, 2, 3, 4, 5, 6]
b = ['apple', 'banana', 'orange']
c = [1, 2, 3.14, 'apple', 'orange']
print(a)
print(b)
print(c)
```
- We can directly call the `list()` constructor to initialise the list.

## Accessing List Elements
```python
a = [10, 20, 30, 40, 50]
print(a[0]) # Accessing the First Element
print(a[-1]) # Accessing the Last Element
```
- The above code snippet shows accessing individual list elements manually.
- To print and access all the list elements in the list, we can use any of the loops.
- While `while`, `for`, `do-while` and various other looping constructs can be used, `for` is the chosen loop.
- The Snippet below demonstrates the accessing of list elements in a `for` loop.
```python
a = [10, 20, 30, 40]
for i in range(len(a)):
  print(a[i])
```
