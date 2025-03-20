# Basic Calculator Program

def main():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user to input a mathematical operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on the user's input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()