from re import S
from typing_extensions import Self


class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b


cal = Calculadora(10, 20)

print(cal.soma())
print(cal.div())
print(cal.mult())
print(cal.sub())


