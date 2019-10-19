from cw2 import zad5
class ScienceCalculator(zad5.Calculator):
    @staticmethod
    def power(liczba1, liczba2):
        return liczba1 ** liczba2

    @staticmethod
    def modulo(liczba1, liczba2):
        return liczba1 % liczba2


print(ScienceCalculator.multiply(-4, -6))
print(ScienceCalculator.power(2, -2))
print(ScienceCalculator.modulo(21, 10))