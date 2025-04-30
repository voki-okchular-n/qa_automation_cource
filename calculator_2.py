from calculator_module import AdvancedCalc
import re

calculator = AdvancedCalc()

while True:
    user_input = input("Введите выражение (например, 3+7): ")
    pattern = r'^(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)$'

    match=re.fullmatch(pattern, user_input)
    if match:
        break
    else:
        print("Вы ввели некорректные значения, попробуйте снова.")

a = float(match.group(1))
operator = match.group(2)
b = float(match.group(3))

operations = {
    "+": calculator.add,
    "-": calculator.subtract,
    "*": calculator.multiply,
    "/": calculator.divide
}

result = operations[operator](a, b)

print("Результат операции: ", result)
