import json


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
    def __init__(self):
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
