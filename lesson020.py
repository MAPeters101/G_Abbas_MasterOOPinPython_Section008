class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + other.num1, self.num2 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num1, self.num2 - other.num2

obj1 = Calculator(3,7)
obj2 = Calculator(4,2)

obj3 = obj1 + obj2
print(obj3)

obj4 = obj1 - obj2
print(obj4)
