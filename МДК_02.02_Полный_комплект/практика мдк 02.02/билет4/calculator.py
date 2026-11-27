from interfaces import InputInterface, OutputInterface


class Calculator:
   
    def __init__(self, input_src: InputInterface, output_dst: OutputInterface):
        self._input = input_src
        self._output = output_dst

    def run(self) -> None:
        if not self._input.is_valid():
            self._output.show_error("Некорректный ввод данных")
            return

        a = self._input.get_operand_a()
        b = self._input.get_operand_b()
        op = self._input.get_operator()

        try:
            result = self._calculate(a, op, b)
            self._output.show_result(result)
        except ZeroDivisionError:
            self._output.show_error("Деление на ноль невозможно")

    def _calculate(self, a: float, op: str, b: float) -> float:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ZeroDivisionError
            return a / b
        raise ValueError(f"Неизвестный оператор: {op}")