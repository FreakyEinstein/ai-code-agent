import sys
from pkg.calculator import Calculator
from pkg.render import render


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py <expression>')
        print('Example: python main.py 3 + 5')
        return

    expression = sys.argv[1:]  # Pass the arguments as a list
    try:
        # Join them inside evaluate
        result = calculator.evaluate(" ".join(expression))
        # Join them inside render
        to_print = render(" ".join(expression), result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
