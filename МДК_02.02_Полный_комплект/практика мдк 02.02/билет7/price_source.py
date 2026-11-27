from interfaces import PriceSourceInterface


class ManualPriceSource(PriceSourceInterface):
    def get_prices(self) -> list[float]:
        raw = input("Введите цены через пробел: ")
        prices = []
        for token in raw.split():
            try:
                prices.append(float(token))
            except ValueError:
                continue
        return prices


class FilePriceSource(PriceSourceInterface):
    def __init__(self, path: str):
        self._path = path

    def get_prices(self) -> list[float]:
        with open(self._path, encoding="utf-8") as f:
            return [float(line.strip()) for line in f if line.strip()]