from input_module import ConsoleInput
from output_module import ConsoleOutput
from calculator import Calculator


def main():
    input_src = ConsoleInput()
    output_dst = ConsoleOutput()

    input_src.read()                  
    calc = Calculator(input_src, output_dst)
    calc.run()                       


if __name__ == "__main__":
    main()