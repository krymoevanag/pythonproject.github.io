num1=float(input("Enter your a number: "))
operation= input("Enter the operation(+,-,*,/)")
num2=float(input("Enter the second number: "))
if operation=="+":
    result= num1+num2
    print(f"{num1} + {num2} ={result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} ={result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  # Checking for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} ={result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
