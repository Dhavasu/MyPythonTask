def add(x, y):
    total_add = x + y
    print(f"Add: {x} + {y} = {total_add}") 
    return total_add    

def subtract(x, y):
    total_sub = x - y
    print(f"Subtract: {x} - {y} = {total_sub}")
    return total_sub

def multiply(x, y):
    total_multi = x * y
    print(f"Multiply: {x} * {y}= {total_multi}")  
    return total_multi 

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")  
    total_divide = x / y
    print(f"Divide: {x} / {y} = {total_divide}")
    return total_divide 
    
def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Factorial: {n}! = {result}")
        return result
