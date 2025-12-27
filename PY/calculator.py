try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Choose Calculation to Perform: \n",
    "1. Add\n",
    "2. Subtract\n",
    "3. Multiply\n",
    "4. Divide\n")
    
    cal = input().strip().lower()
        
    if cal == "Add":
        ans = num1 + num2
    elif cal == "Subtract":
        ans = num1 - num2
    elif cal == "Multiply":
        ans = num1 * num2
    elif cal == "Divide":
        if num2 == 0:
            print("Error: Can't divide by zero.")
            ans = None
        else:
            ans = num1 / num2
    else:
        print("Invalid operation selected.")
        
    if ans is not None:
        print(f"The Answer is: {ans}")
except ValueError:
    print("Invalid input. Please enter valid number!")