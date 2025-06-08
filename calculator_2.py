import math
import random
import re
from collections import Counter

from calculator_module import AdvancedCalc, ZeroError
from calculator_module import Timer, factorial

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
    calculator.log_to_file("error", {
        "error_type": "ZeroError",
        "message": str(error)
    })


except IndexError as error:
    print("Ошибка памяти:", error)
    calculator.log_to_file("error", {
        "error_type": "IndexError",
        "message": str(error)
    })

print("\nВремя необходимое для вычисления больших факториалов:")
print("Время для факториала 100:")
with Timer():
    factorial(100)

print("\nСравнение времени для факториала 1000:")

print("Время для факториала 1000 первый раз без кэша:")
with Timer():
    factorial(1000)

print("Время для факториала 1000 с кэшем:")
with Timer():
    factorial(1000)

print("Время с использованием math.factorial:")
with Timer():
    math.factorial(1000)

print("\nГенерируем 1000 случайных чисел от 1 до 10:")

numbers = []
for i in range(1000):
    numbers.append(random.randint(1, 10))

counts = Counter(numbers)

print("Итоги генерации чисел:")
for number, count in sorted(counts.items()):
    print(f"Число {number}: выпало {count} раз")
