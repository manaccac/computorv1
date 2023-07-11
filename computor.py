import sys
import re
import function as function

if len(sys.argv) != 2:
    print("Please provide an equation as a command line argument")
    print("Use -help for more information")
    sys.exit(1)

equation = sys.argv[1]

if equation == "-help":
    print("Usage: python3 computor.py equation\n")
    print("Enter the equation in the following format:")
    print("- Use '*' for multiplication, e.g., 5*X^2")
    print("- Use '/' for division, e.g., 2/3*X")
    print("- Use '^' for exponentiation, e.g., X^3")
    print("- Separate terms with '+' or '-', e.g., 2*X - 5*X^2 + 3")
    print("- Place the equation on both sides of the equal sign, e.g., 2*X = 0")
    sys.exit(0)

tmp = equation

equation = function.syntax(equation)

if equation == -1:
    print("Syntax error")
    print("Use -help for more information")

    sys.exit(1)

print(tmp)
equation = equation.split("=")
left_equation = equation[0]
right_equation = equation[1]
left_equation = re.split(r"(\+|-)", left_equation)
right_equation = re.split(r"(\+|-)", right_equation)

left_equation = function.cut_equation(left_equation)
right_equation = function.cut_equation(right_equation)
equation = function.reduced_form(left_equation, right_equation)
equation_degree = function.get_degree(equation)

function.solve_equation(equation)
