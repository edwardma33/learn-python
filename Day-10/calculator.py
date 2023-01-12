import os
def clear():
    os.system("clear")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for operator in operations:
    print(operator)
operator = input("pick an operator from the line above: ")
num2 = int(input("What's the second number?: "))
calc_operation = operations[operator]
answer = calc_operation(num1, num2)

clear()

print(answer)

while input("Would you like to do another operation?: [y/n]: ") == "y":
    for operator in operations:
        print(operator)
    calc_operation = operations[input("Pick an operator from the line above: ")]
    answer = calc_operation(answer, int(input("What's the next number?: ")))
    print(answer)