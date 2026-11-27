from abc import ABC, abstractmethod


class PriceSourceInterface(ABC):
    @abstractmethod
    def get_prices(self) -> list[float]: ...


class SumCalculatorInterface(ABC):
    @abstractmethod
    def calculate_sum(self, prices: list[float]) -> float: ...


class OutputInterface(ABC):
    @abstractmethod
    def show_result(self, total: float) -> None: ...

    @abstractmethod
    def show_error(self, message: str) -> None: ...