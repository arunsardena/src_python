class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

# Create an instance of the Calculator class
calculator = Calculator()

# Perform calculations using the class methods
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(8, 2)
result_multiply = calculator.multiply(4, 6)
result_divide = calculator.divide(9, 3)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)