class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

obj1 = Calculator(3,7)
obj2 = Calculator(4,2)

obj3 = obj1 + obj2
print(obj3)
