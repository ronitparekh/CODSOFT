def calculator():
    while True:
        try:
            num1_input = input("Enter the first number (or 'q' to quit): ")
            if num1_input.lower() == 'q':
                break
            num1 = float(num1_input)
            num2 = float(input("Enter the second number: "))
            
            print("Choose the operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation = input("Enter the number corresponding to the operation (or 'q' to quit): ")

            if operation == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif operation == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif operation == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif operation.lower() == 'q':
                break
            else:
                print("Invalid operation choice.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            
calculator()