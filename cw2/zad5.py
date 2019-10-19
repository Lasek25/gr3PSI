class Calculator:
    @staticmethod
    def add(liczba1, liczba2):
        return liczba1 + liczba2

    @staticmethod
    def difference(liczba1, liczba2):
        return liczba1 - liczba2

    @staticmethod
    def multiply(liczba1, liczba2):
        return liczba1 * liczba2

    @staticmethod
    def divide(liczba1, liczba2):
        if liczba2 != 0:
            return liczba1 / liczba2
        return "Dividing by zero is forbidden!"


#print(Calculator.add(3, 3))
#print(Calculator.difference(3, -13))
#print(Calculator.multiply(-4, 3))
#print(Calculator.divide(3, 2))

