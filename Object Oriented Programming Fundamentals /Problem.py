class ArithmeticOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed."

    # Operator Overloading for >
    def __gt__(self, other):
        return (self.a + self.b) > (other.a + other.b)

    # Operator Overloading for <
    def __lt__(self, other):
        return (self.a + self.b) < (other.a + other.b)

# Example usage:
operation1 = ArithmeticOperations(10, 5)
operation2 = ArithmeticOperations(7, 4)

print("Addition:", operation1.add())
print("Subtraction:", operation1.subtract())
print("Multiplication:", operation1.multiply())
print("Division:", operation1.divide())

# Demonstrating > and <
if operation1 > operation2:
    print("Operation1 is greater than Operation2.")
else:
    print("Operation1 is not greater than Operation2.")

if operation1 < operation2:
    print("Operation1 is less than Operation2.")
else:
    print("Operation1 is not less than Operation2.")
