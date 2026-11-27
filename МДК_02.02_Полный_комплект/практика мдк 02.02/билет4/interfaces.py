from abc import ABC, abstractmethod


class InputInterface(ABC):
 
    @abstractmethod
    def get_operand_a(self) -> float: ...

    @abstractmethod
    def get_operand_b(self) -> float: ...

    @abstractmethod
    def get_operator(self) -> str: ...

    @abstractmethod
    def is_valid(self) -> bool: ...


class OutputInterface(ABC):

    @abstractmethod
    def show_result(self, value: float) -> None: ...

    @abstractmethod
    def show_error(self, message: str) -> None: ...