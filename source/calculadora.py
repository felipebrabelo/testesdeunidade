
class Calculadora:
    def __int__(self):
        pass
    @staticmethod
    def soma(a, b):
        return a + b
    @staticmethod
    def subtracao(a, b):
        return a - b
    @staticmethod
    def multiplicacao(a, b):
        return a * b
    @staticmethod
    def divisao(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ZeroDivisionError("Divisão por zero não permitida.")
