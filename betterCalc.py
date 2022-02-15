firstNumber = input("Enter the first number: ")
operator = input("Enter the operator ('+,*,-,/ or %) you want to use: ")
secondNumber = input("Enter the second number: ")

def calc(firstNumber, operator, secondNumber):
    if operator == "+":
       return (float(firstNumber) + float(secondNumber))
    elif operator == "*":
       return (float(firstNumber) * float(secondNumber))
    elif operator == "-":
       return (float(firstNumber) - float(secondNumber))
    elif operator == "/":
       return (float(firstNumber) / float(secondNumber))
    elif operator == "%":
       return (float(firstNumber) % float(secondNumber))   
    else:
       return print("Invalid operator")  


result = calc(firstNumber, operator, secondNumber)

print(f"{firstNumber} {operator} {secondNumber} equals {result}")
