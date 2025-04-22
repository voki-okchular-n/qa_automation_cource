import re

def add (a, b=None):
    if b is None:
        return sum(a)
    else:
        return a + b

def subtract (a, b):
    return a + b

def divide (a, b):
    return a / b

def multiply (a, b):
    return a * b

while True:
    user_input = input("Введите значения (например, 3+7)")
    pattern = r'^\d+(\.\d+)?[+\-*/]\d+(\.\d+)?$'
    if re.fullmatch(pattern,user_input):
        break
    else:
        print ("Вы ввели некорректные значения, попробуйте снова")

for char in user_input:
    if char in "-+/*":
        operator = char
        break
number1, number2 = user_input.split(operator)
a = float(number1)
b = float(number2)

all_operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

result = all_operations[operator](a, b)
print ("Результат операции:", result)