# Functions
- We can hide the details of any computation by defining a function.
- A function definition requires a name, a group of parameters, and a body.
- It may also explicitly return a value. For example, the simple function defined below returns the square of the value you pass into it.

``` python
def square(n):
  return n ** 2
```
<hr/>

# Solving a Problem
You may have heard of the infinite monkey theorem? 

The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the com
plete works of William Shakespeare. 

Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel.”

The way we will simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We will write
another function that will score each generated string by comparing the randomly generated
string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string. To make
it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

## Solution
``` python
import random
import string

def generate(length):
    characters = string.ascii_letters + ' '  # Include spaces
    return ''.join(random.choice(characters) for _ in range(length))

def score(sentence):
    string_attempt = generate(len(sentence))
    if string_attempt == sentence:
        return True
    return False

target = "methinks it is like a weasel"

for i in range(100000):
    if score(target):
        print(f"Success on attempt {i+1}")
        break
else:
    print("Target string not found in 100000 attempts.")
```
