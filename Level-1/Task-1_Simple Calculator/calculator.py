def addition(a, b):
    return a + b        # returns sum of both no.s

def subtraction(a, b):
    return a - b        # returns subtracted result

def multiplication(a, b):
    return a * b            # returns product of two no.s

def division(a, b):
    if b == 0:
        return "Error: Division by zero"            # error if divided by zero
    return a / b            # return division result


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1/2/3/4): ")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", addition(a, b))
        elif choice == '2':
            print("Result:", subtraction(a, b))
        elif choice == '3':
            print("Result:", multiplication(a, b))
        elif choice == '4':
            print("Result:", division(a, b))
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers")


if __name__ == "__main__":
    main()