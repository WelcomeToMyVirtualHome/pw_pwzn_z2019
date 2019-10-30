"""
Część 1 (1 pkt): Uzupełnij klasę Calculator
tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (memory, atrybut klasy) z interfejsem: dodaj do pamięci , wyczyść pamięć.
Atrybut memory ma być nienadpisywalny.
Część 2 (1 pkt): jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obsłuż przypadki skrajne.
"""
from operator import add, sub, mul, truediv

class Calculator:
    def __init__(self):
        self._memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji, tak by metoda memorize przypisywała
        # wynik zapisany w tym atrybucie
        self._short_memory = None
        self.operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : truediv
        }

    def run(self, operator, arg1, arg2 = None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        
        if arg1 is None:
            raise ValueError
        flag = False
        if arg2 is None:
            if self.memory is None:
                raise Exception
            arg2 = self.memory
            flag = True
        if operator is None:
            raise ValueError
        
        if operator == "/":
            if flag and arg1 == 0:
                raise ValueError
            if not flag and arg2 == 0:
                raise ValueError

        self._short_memory = self.operations[operator](arg1, arg2)
        return self._short_memory

    @property
    def memory(self):
        return self._memory

    def memorize(self):
        """Saves last operation result to memory."""
        self._memory = self._short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._memory = None

    def in_memory(self):
        """Prints memorized value."""
        print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    calc = Calculator()
    b = calc.run('+', 1, 2)
    calc.memorize()
    calc.in_memory()
    c = calc.run('/', 3)
    # assert c == 3