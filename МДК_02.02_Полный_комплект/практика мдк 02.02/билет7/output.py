from interfaces import OutputInterface


class ConsoleOutput(OutputInterface):
    def show_result(self, total: float) -> None:
        print(f"Итоговая сумма: {total:.2f} руб.")

    def show_error(self, message: str) -> None:
        print(f"Ошибка: {message}")