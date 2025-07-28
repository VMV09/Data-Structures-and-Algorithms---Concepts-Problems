# Basic Data Structures 
## Objectives
1. Understand abstract data types stack, queues, and list.
2. Implement the ADTs stack, queue, and deque using Python lists.
3. Understand the performance of the implementations of basic linear data structures.
4. Understand prefix, infix, and postfix expression formats.
5. Use stacks for evaluation of these expression formats.
6. Use queues for basic timing simulations.
7. Ability to recognize problem properties where stacks, queues, and deques are appropriate data structures.
8. Ability to implement the abstract data type list as a linked list using the node and reference pattern.
9. Ability to compare the performance of our linked list implementation with Python’s list implementation.
## Linear Structures
- Stacks, queues, deques, and lists are examples of data collections whose items are ordered depending on how they are added or removed.
- Once an item is added, it stays in that position relative to the other elements that came before and came after it.
- Collections such as these are often referred to as linear data structures.
- What differentiates one linear data structure from another is the way in which items are added and removed, in particular location where these additions and removals occur.
- These appear in many algorithms and can be used to solve a variety of important problems.
### Stacks
- A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
- This end is commonly referred to as the “top.”
- The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest.
- The most recently added item is the one that is in position to be removed first. This ordering principle is sometimes called LIFO, last-in first-out.
- It provides an ordering based on length of time in the collection.
-  Stacks are fundamentally important, as they can be used to reverse the order of items.
-  The order of insertion is the reverse of the order of removal.
- `For example, every web browser has a Back button. As you navigate
 from web page to web page, those pages are placed on a stack (actually it is the URLs that are
 going on the stack). The current page that you are viewing is on the top and the first page you
 looked at is at the base. If you click on the Back button, you begin to move in reverse order
 through the pages.`
- The stack operations are given below.
     - `Stack()`: creates a new empty task. Needs no parameter and returns an empty stack.
     - `push(item`: adds a new item to the top of the stack. It needs the item and return nothing.
     - `pop()`: removes the top item from the stack. It needs no parameters and returns the item.
     - `peek()`: returns the top item from the stack but does not remove it. It needs no parameters and returns a boolean value.
     - `is_empty()`: tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
     - `size()`: returns the number of items on the stack. It needs no parameters and returns an integer.
- **Implementing Stack in Python**
```python
# The implementation of choice of an abstract data type such as a stack is the creation of a new class.
# The stack operations are implemented as methods.
# Further, to implement a stack, which is a collection of elements, it makes sense to utilize the power and # simplicity of the primitive collections provided by Python.
# We will use a list.
class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, items):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)
```
