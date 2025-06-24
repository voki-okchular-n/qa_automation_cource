import json
import time
from datetime import datetime


class ZeroError(ZeroDivisionError):
    def __init__(self, error_message="Невозможно делить на ноль - ошибка"):
        super().__init__(error_message)


class BasicCalc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


class AdvancedCalc(BasicCalc):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "memory"):
            self.memory = []

    def memo_plus(self, new_value):
        if len(self.memory) >= 3:
            self.memory.pop(0)
        self.memory.append(new_value)

    def memo_minus(self):
        if not self.memory:
            raise IndexError("Память пуста — невозможно извлечь значение")
        return self.memory.pop()

    @property
    def top(self):
        if not self.memory:
            raise IndexError("Память пуста — невозможно достать top значения")
        return self.memory[-1]

    def convert_to_float(self, pre_value):
        try:
            return float(pre_value)
        except (TypeError, ValueError):
            return 0

    def log_to_file(self, log_type, data):
        log_data = {
            "type": log_type,
            "timestamp": datetime.now().isoformat(),
            **data
        }
        with open("calculator.log", "a", encoding="utf-8") as file:
            file.write(json.dumps(log_data) + "\n")

    def _calculate(self, operation, a, b):
        if b is None:
            b = a
            a = self.top

        a = self.convert_to_float(a)
        b = self.convert_to_float(b)

        if operation == super().divide and b == 0:
            raise ZeroError()

        result = operation(a, b)
        self.memo_plus(result)

        self.log_to_file("operation", {
            "operation": operation.__name__,
            "inputs": [a, b],
            "result": result
        })

        return result

    def add(self, a, b=None):
        return self._calculate(super().add, a, b)

    def subtract(self, a, b=None):
        return self._calculate(super().subtract, a, b)

    def multiply(self, a, b=None):
        return self._calculate(super().multiply, a, b)

    def divide(self, a, b=None):
        return self._calculate(super().divide, a, b)


class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Считаем:")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start
        print(f"Итог по времени: {duration:.2f} секунд")


def factorial_generator(limit):
    factorial_result = 1
    for n in range(1, limit + 1):
        factorial_result *= n
        yield n, factorial_result


def decorator_with_cache(cache):
    def decorator(func):
        def cached_func(n):
            if n in cache:
                return cache[n]
            factorial_result = func(n)
            cache[n] = factorial_result
            return factorial_result

        return cached_func

    return decorator


factorial_cache = {}
for n, factorial_value in factorial_generator(1000):
    factorial_cache[n] = factorial_value


@decorator_with_cache(factorial_cache)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
