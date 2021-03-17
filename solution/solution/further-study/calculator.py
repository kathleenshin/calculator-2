"""A prefix-notation calculator."""

from arithmetic import *

input_file = open("operations.txt")
output_file = open("results.txt", 'a')

for line in input_file:
    tokens = line.split()

    if len(tokens) < 2:
        print("Warning: Not enough inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    if not num1.isdigit() or not num2.isdigit():
        output_file.write("Those aren't numbers!")
        continue

    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    else:
        print("Warning: Not all commands are in the correct format.")
        continue

    output_file.write(str(result) + "\n")

output_file.close()
