# Simple Calculator (Console)

def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation.")

        print("Result:", result)

    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)

if __name__ == "__main__":
    calculator()
