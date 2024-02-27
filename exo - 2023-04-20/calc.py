class Calculator:
    def __init__(self, initial_value):
        self.result = initial_value

    def add(self, value):
        self.result += value
        return self.result

    def sub(self, value):
        self.result -= value
        return self.result

    def mult(self, value):
        self.result *= value
        return self.result

    def div(self, value):
        self.result /= value
        return self.result

    def reset(self):
        self.result = 0




# -- main program --

calc = Calculator(15)
print(calc.mult(2))
print(calc.div(6))
print(calc.result)
