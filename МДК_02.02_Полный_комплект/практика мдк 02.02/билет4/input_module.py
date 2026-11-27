from interfaces import InputInterface


class ConsoleInput(InputInterface):

    VALID_OPERATORS = {"+", "-", "*", "/"}

    def __init__(self):
        self._a = 0.0
        self._b = 0.0
        self._op = ""
        self._valid = False

    def read(self) -> None:
       
        try:
            self._a = float(input("Введите первое число: "))
            self._op = input("Введите оператор (+ - * /): ").strip()
            self._b = float(input("Введите второе число: "))
            self._valid = self._op in self.VALID_OPERATORS
        except ValueError:
            self._valid = False

    def get_operand_a(self) -> float:
        return self._a

    def get_operand_b(self) -> float:
        return self._b

    def get_operator(self) -> str:
        return self._op

    def is_valid(self) -> bool:
        return self._valid