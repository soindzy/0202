from interfaces import OutputInterface


class ConsoleOutput(OutputInterface):

    def show_result(self, value: float) -> None:

        formatted = int(value) if value == int(value) else value
        print(f"Результат: {formatted}")

    def show_error(self, message: str) -> None:
        print(f"Ошибка: {message}")