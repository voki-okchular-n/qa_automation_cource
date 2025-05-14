from calculator_module import AdvancedCalc, ZeroError
import re
import json

calculator = AdvancedCalc()

while True:
    user_input = input("Введите выражение (например, 3+7): ")
    pattern = r'^(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)$'

    match = re.fullmatch(pattern, user_input)
    if match:
        break
    else:
        print("Вы ввели некорректные значения, попробуйте снова.")

a = match.group(1)
operator = match.group(2)
b = match.group(3)

operations = {
    "+": calculator.add,
    "-": calculator.subtract,
    "*": calculator.multiply,
    "/": calculator.divide
}

try:
    result = operations[operator](a, b)
    print("Результат операции: ", result)

    print("В памяти: ", calculator.memory)
    print("top значение в памяти: ", calculator.top)

    removed_value = calculator.memo_minus()
    print("Значение, извлеченное из памяти: ", removed_value)
    print("В памяти после удаления: ", calculator.memory)

except ZeroError as error:
    print("Ошибка деления:", error)
    log_data = {
        "error": ZeroError,
        "message": str(error)
    }
    with open("calculator.log", "a", encoding="utf-8") as file:
        file.write(json.dumps(log_data) + "\n")

except IndexError as error:
    print("Ошибка памяти:", error)
    log_data = {
        "error": IndexError,
        "message": str(error)
    }
    with open("calculator.log", "a", encoding="utf-8") as file:
        file.write(json.dumps(log_data) + "\n")
