class BasicCalc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract (a, b):
        return a - b

    @staticmethod
    def multiply (a, b):
        return a * b

    @staticmethod
    def divide (a, b):
        return a / b

class AdvancedCalc(BasicCalc):
    def __init__(self):
        self.memory = []

    def memo_plus(self, new_value):
        if len(self.memory) >= 3:
            self.memory.pop(0)
        self.memory.append(new_value)

    def memo_minus(self):
        return self.memory.pop() if self.memory else None

    @property
    def top(self):
        return self.memory[-1] if self.memory else None

    def _calculate(self, operation, a, b):
        b = b or self.top
        result = operation(a, b)
        self.memo_plus(result)
        return result

    def add(self, a, b=None):
        return self._calculate(super().add, a, b)

    def subtract(self, a, b=None):
        return self._calculate(super().subtract, a, b)

    def multiply(self, a, b=None):
        return self._calculate(super().multiply, a, b)

    def divide(self, a, b=None):
        return self._calculate(super().divide, a, b)
