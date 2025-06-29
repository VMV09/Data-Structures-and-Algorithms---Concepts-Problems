# Exception Handling in Python
- There are two types of errors that typically occur when writitng programs.
- Syntax Errors and Runtime Errors.
- Syntax Errors occurs when a programmer or developer has made a mistake in the structure of a statement or expression.
- For Example, the code snippet below depicts a Syntax Error:
``` python
for i in range(10)
```
-  In this case, the Python interpreter has found that it cannot complete the processing of this instruction since it does not conform to the rules of the language.
-  Syntax errors are usually more frequent when you are first learning a language.
-  The other error which is called Runtime or Logic Error denotes a situation where the program executes without an syntactical errors but often fails to output the correct results.
-  This could be the issue in the core logic used to solve the problem or the way in which the core logic is implemented.
-   In some cases, logic errors lead to very bad situations such as trying to divide by zero or trying to access an item in a list where the index of the item is outside the bounds of the list.
-   In this case, the logic error leads to a runtime error that causes the program to terminate. These types of runtime errors are typically called exceptions.
-   Most programming languages provide a way to deal with these errors that will allow the programmer to have some type of intervention if they so choose.
-   In addition, programmers can create their own exceptions if they detect a situation in the program execution that warrants it.
-   We can handle the exception that has been raised by using the `try` statement.
-   Run the below code to analyse the exception raised.
``` python
a_number = int(input("Please enter an integer"))
print(math.sqrt(a_number))
```
- We handle this exception by calling the print function withing a try block, and a corresponding except block catches the exception, orints the message within except and continues program execution.
``` python
number = int(input("Please enter an integer"))
try:
  print(math.sqrt(number))
except:
  print("Negative Number for Square Root")
  print(math.sqrt(abs(number)))
```
- Python provides provisions for the programmer to cause a runtime exception by using the `raise` statement.
- Instead of calling the square root function with a negative number, we could have checked the value first and then raised our own exception.
- The code snippet below shows the result of creating a new RuntimeError exception.
- `Note that the program would still terminate but now the exception that caused the termination is something explicitly created by the programmer.`
``` python
if number < 0:
  raise RuntimeError("YOu cannot enter a negative number")
else:
  print(math.sqrt(number))
```
- You can see the Python reference manual for a list of all the available exception types and for
 how to create your own exceptions and raises.

**YOU ARE ADVISED TO EXECUTE ALL THE CODE SNIPPETS FOR GAINING CLARITY AND CONCEPTUAL UNDERSTANDING.**
**ALSO FEEL FREE TO CHANGE AND MANIPULATE THE CODE SNIPPETS ON YOU OWN AND TRY TO LEARN THE BEHAVIOUR OF THE PROGRAM UNDER THESE MODIFICATIONS.**
