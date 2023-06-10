#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        opp = sys.argv[2]
        b = int(sys.argv[3])

        if opp == "+":
            result = add(a, b)
        elif opp == "-":
            result = sub(a, b)
        elif opp == "*":
            result = mul(a, b)
        elif opp == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print(f"{a} {opp} {b} = {result}")
