def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 5:
            break
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print(num1 + num2)
        elif choice == 2:
            print(num1 - num2)
        elif choice == 3:
            print(num1 * num2)
        elif choice == 4:
            if num2==0:
                print("Invalid Input: Denominator should not be zero")
            else:
                print(num1 / num2)
        else:
            print("Invalid Input")

calculator()