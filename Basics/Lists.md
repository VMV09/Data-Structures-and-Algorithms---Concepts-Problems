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
## Adding Elements to the List
- There are various methods and logics to add elements to a list.
- We shall first initialise an empty list.
- Python provides a built-in function `append()` to add an element to the list. The element to be added is specified within the paraentheses of the `append` function.
``` python
a = []
a.append(10)
print(a)
```
- Another important and well used function is `insert()`.
- The function takes the position in the list where the element is to be inserted as well as the element to be inserted into the list.
- The below code inserts at position 0, the element 5.
``` python
a = []
a.insert(0, 5)
print(a)
```
- The last method the python provides to add elements to the list is the `extend()` function.
- The `extend()` function works very similar to the `append()`, but the only flexibility that `extend` provides is - while `append` can add single individual element, `extend()` can add multiple elements in one go to the list.
- Check the code below.
``` python
a = []
a.extend([15, 20, 25])
print(a)
```
- It is worth noting that `insert()` takes O(n) time to execute, while `append()` runs in a constant time o(1). **For more detailed view on performance of data structure in python, refer `PerformanceofDataStrucutres.md`.**
- **It is important to remember that both `append()` and `extend()` adds elements at the end of the list only.**
- **To insert the element at a position of our desire, we are obliged to use the `insert()` function.**
