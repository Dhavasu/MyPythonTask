# math_operations.py (fixed)

def add(a, b):
    """Return the sum of a and b."""
    result = a + b  # Corrected to remove +1
    print(f"add({a}, {b}) = {result}")  # Debug output
    return result

def subtract(a, b):
    """Return the difference of a and b."""
    result = a - b
    print(f"subtract({a}, {b}) = {result}")  # Debug output
    return result

def multiply(a, b):
    """Return the product of a and b."""
    result = a * b
    print(f"multiply({a}, {b}) = {result}")  # Debug output
    return result

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
