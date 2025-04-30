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
        if self.memory:
            return self.memory.pop()
        return None

    @property
    def top(self):
        return self.memory[-1]

    def add(self, a, b=None):
        if b is None:
            b = a
            a = self.top
        result = super().add(a, b)
        self.memo_plus(result)
        return result

    def subtract(self, a, b=None):
        if b is None:
            b = a
            a = self.top
        result = super().subtract(a, b)
        self.memo_plus(result)
        return result

    def multiply(self, a, b=None):
        if b is None:
            b = a
            a = self.top
        result = super().multiply(a, b)
        self.memo_plus(result)
        return result

    def divide(self, a, b=None):
        if b is None:
            b = a
            a = self.top
        result = super().divide(a, b)
        self.memo_plus(result)
        return result
