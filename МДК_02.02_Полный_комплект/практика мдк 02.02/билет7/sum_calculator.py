from interfaces import SumCalculatorInterface


class SumCalculator(SumCalculatorInterface):
    def calculate_sum(self, prices: list[float]) -> float:
        if not prices:
            raise ValueError("Список цен пуст")
        if any(p < 0 for p in prices):
            raise ValueError("Цена не может быть отрицательной")
        return sum(prices)