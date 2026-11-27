from price_source import ManualPriceSource
from sum_calculator import SumCalculator
from output import ConsoleOutput


def main():
    source = ManualPriceSource()
    calculator = SumCalculator()
    output = ConsoleOutput()

    prices = source.get_prices()

    try:
        total = calculator.calculate_sum(prices)
    except ValueError as e:
        output.show_error(str(e))
        return

    output.show_result(total)


if __name__ == "__main__":
    main()