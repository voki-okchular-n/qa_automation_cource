import re

def add (a, b=None):
    if b is None:
        return sum(a)
    else:
        return a + b

def subtract (a, b):
    return a - b

def divide (a, b):
    return a / b

def multiply (a, b):
    return a * b

def calculation(user_input):
    pattern = r'^(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)$'
    match = re.fullmatch(pattern, user_input)
    a = float(match.group(1))
    operator = match.group(2)
    b = float(match.group (3))

    all_operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
    }

    result = all_operations[operator](a, b)
    return f"Результат операции: {result}"

if __name__ == "__main__":
    while True:
        user_input = input("Введите значения (например, 3+7): ")
        pattern = r'^(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)$'

        if re.fullmatch(pattern,user_input):
            break
        else:
            print ("Вы ввели некорректные значения, попробуйте снова")

    result_message = calculation(user_input)
    print(result_message)
    