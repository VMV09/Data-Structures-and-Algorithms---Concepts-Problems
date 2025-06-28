# The object Oriented Programming in Python.
- Python is a both procedural and object-oriented programming language.
- A powerful feature of any OOPs language is the ability to allow a programmer to create a new class that model data that is needed to solve the problem.
- By building a class that implements an abstract data type, a programmer can take advantage of the abstraction process and at the
same time provide the details necessary to actually use the abstraction in a program.
- Whenever we want to implement an abstract data type, we will do so with a new class.

## A Fraction Class
```
class Fraction:
  # the methods go here
```
- The first method that all classes should provide is the constructor.
- The constructor defines the way in which data objects are created.
- To create a `Fraction` object, we will need to provide two pieces of data - the numerator, and the denominator.
- In Python, the constructor method is always called `__init__`.

```
class Fraction:
  def __init__(self, top, bottom):
      self.num = top
      self.den = bottom
```

- The Formal Parameters i.e. the list of parameters passed to the constructor `__init__`.
  - Self is a **special parameter** that will always be used to as a reference back to the object itself.  It must always be the first formal parameter; **however, it will never be given an actual parameter valueupon invocation.**
  -  The notation self.num in the constructor defines the fraction object to have an internal data object called num as part of its state. Likewise, **self.den creates the denominator.**
