#!/usr/bin/env python3
"""
Simple Interactive Calculator
Supports basic arithmetic operations: +, -, *, /
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("Operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  q : Quit")
    print("=" * 40)
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        try:
            # Get user input
            num1 = float(input("\nEnter first number (or 'q' to quit): "))
            operation = input("Select operation (+, -, *, /): ").strip()
            
            if operation.lower() == 'q':
                print("\nThanks for using the calculator!")
                break
            
            if operation not in operations:
                print("Invalid operation! Please use +, -, *, or /")
                continue
            
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            result = operations[operation](num1, num2)
            print(f"\n{num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input! Please enter valid numbers. Error: {e}")

if __name__ == "__main__":
    calculator()
