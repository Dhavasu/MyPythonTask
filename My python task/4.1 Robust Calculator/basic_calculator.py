import math

class Calculator:
    def __init__(self):
        pass

    def Add(self, a, b):
        try:
            add = a + b
            return add
        except:
            print("Error: Invalid input type. Both arguments must be numbers.")
            return None

    def Subtract(self, a, b):
        try:
            sub = a - b
            return sub
        except:
            print("Error: Invalid input type. Both arguments must be numbers.")
            return None

    def Multiply(self, a, b):
        try:
            multiply = a * b
            return multiply
        except:
            print("Error: Invalid input type. Both arguments must be numbers.")
            return None

    def Divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            divide = a / b
            return divide
        except ZeroDivisionError as e:
            print(e)
            return None
        except:
            print("Error: Invalid input type. Both arguments must be numbers.")
            return None

    def square_root(self, x):
        try:
            if x < 0:
                print("Cannot calculate the square root of a negative number.")
                return None
            sr = math.sqrt(x)
            return sr
        except TypeError:
            print("Invalid input: argument must be a number.")
            return None

    def exponentiate(self, x, y):
        try:
            exp = math.pow(x, y)
            if exp == float('inf') or exp == float('-inf'):
                raise OverflowError("Result exceeds maximum limit.")
            return exp
        except OverflowError as i:
            print(i)
            return None
        except TypeError:
            print("Invalid input: both arguments must be numbers.")
            return None

    def logarithm(self, x, base=math.e):
        try:
            if x <= 0:
                raise ValueError("Logarithm undefined for non-positive numbers.")
            Log = math.log(x, base)
            return Log
        except ValueError as i:
            print(i)
            return None
        except:
            print("Invalid input: arguments must be numbers.")
            return None


def get_user_input():
    calculator = Calculator()
    
    while True:
        print("\nAvailable operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exponentiate")
        print("7. Logarithm")
        print("8. Exit")
        
        choice = input("Choose an operation (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {calculator.Add(a, b)}")
                elif choice == '2':
                    print(f"Result: {calculator.Subtract(a, b)}")
                elif choice == '3':
                    print(f"Result: {calculator.Multiply(a, b)}")
                elif choice == '4':
                    print(f"Result: {calculator.Divide(a, b)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                a = float(input("Enter number: "))
                print(f"Result: {calculator.square_root(a)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {calculator.exponentiate(base, exponent)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            try:
                a = float(input("Enter number: "))
                base = input("Enter base (default is e): ")
                if base:
                    base = float(base)
                    print(f"Result: {calculator.logarithm(a, base)}")
                else:
                    print(f"Result: {calculator.logarithm(a)}")

            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid choice. Please select a valid operation.")

# Run the calculator
if __name__ == "__main__":
    get_user_input()
