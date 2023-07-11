import math

def ft_abs(nb):
    if nb < 0:
        return(-nb)
    else:
        return(nb)

def ft_sqrt(nb):
    return(float(nb ** 0.5))

def ft_swap(a, b):
    tmp = a
    a = b
    b = tmp
    return(a, b)

def print_equation(equation):
    i = get_degree(equation)
    while(i >= 0):
        if i < get_degree(equation) and equation[i] > 0:
            print("+", end = " ")
        elif equation[i] < 0:
            print("-", end = " ") if i == get_degree(equation) else print("-", end = " ")
        if not equation[i] == 0:
            coeff = int(equation[i]) if equation[i].is_integer() else equation[i]
        if not equation[i] == 0 and ft_abs(equation[i]) != 1:
            if i > 1:
                print(f"{ft_abs(coeff)} * X^{i}", end = " ")
            elif i == 1:
                print(f"{ft_abs(coeff)} * X", end = " ")
            elif i == 0:
                print(f"{ft_abs(coeff)}", end = " ")
        elif ft_abs(equation[i]) == 1:
            if i > 1:
                print(f"X^{i}", end = " ")
            elif i == 1:
                print(f"X", end = " ")
            elif i == 0:
                print(f"{ft_abs(coeff)}", end = " ")
        if get_degree(equation) == 0 and equation[0] == 0:
            print("0", end = " ")
        i -= 1

def ft_fraction(dec):
    num = int(str(dec).split(".")[1])
    denom = int("1" + (len(str(num))) * "0")
    rest = int(str(dec).split(".")[0])
    div = num

    if denom >= 1000:
        return(str(dec))
    while (div > 0):
        if (num % div == 0 and denom % div == 0):
            break
        div -= 1
    if rest < 0:
        return(f"-{int((num - rest * denom) / div)}/{int(denom / div)}")
    else:
        return(f"{int((num + rest * denom) / div)}/{int(denom / div)}")

def print_solution(solution):
    if solution == 0:
        print(ft_abs(int(solution)))
    elif solution.is_integer():
        print(int(solution))
    else:
        print(ft_fraction(solution))

def syntax(equation):
    equation = equation.replace(' ', '')

    close = True
    equal_sign = False
    has_x = False
    only_digits = True
    i = 0

    if (equation == ""):
        return -1

    while i < len(equation):
        
        char = equation[i]
        next_char = equation[i + 1] if i + 1 < len(equation) else None

        if char.isdigit():
            if next_char and next_char.lower() == 'x':
                return -1  # A digit is followed by an 'x' without an operator in between
        elif char == '=':
            if close and not equal_sign:
                equal_sign = True
            else:
                return -1
        elif char == '(':
            close = False
        elif char in '-+^*/' and next_char and (next_char.isdigit() or next_char.lower() == 'x'):
            only_digits = False
        elif char == '.' and next_char and next_char.isdigit():
            pass
        elif char.lower() == 'x':
            has_x = True
            only_digits = False
            if next_char and (next_char.lower() == 'x' or next_char.isdigit()):
                return -1
        elif char == ')':
            close = True
        else:
            return -1

        i += 1

    if not close or not equal_sign or not has_x or only_digits:
        return -1

    return equation


def cut_equation(equation):
    index_coeff = []
    i = 0
    for element in equation:
        if not element == "+" and not element == "-" and not len(element) == 0:
            if '/' in element:
                element = str(eval(element))
            element = element.split("*")
            if len(element) > 2:
                exit()
            elif len(element) == 1:
                if element[0].lower().startswith("x"):
                    element.insert(0, "1")
                    power = element[1].lower().lstrip("x^") if '^' in element[1] else 1
                else:
                    power = 0
            else:
                if 'x' in element[1].lower():
                    power = element[1].lower().lstrip("x^") if '^' in element[1] else 1
                else:
                    power = 0
            if equation[i - 1] == "+" or equation[i - 1] == "-":
                coeff = equation[i - 1] + element[0]
            else:
                coeff = element[0]
            if len(index_coeff) - 1 >= int(power):
                index_coeff[int(power)] += float(coeff)
            else:
                while len(index_coeff) <= int(power):
                    index_coeff.append(0)
                index_coeff[int(power)] = float(coeff)
        i += 1
    return index_coeff





def reduced_form(left_equation, right_equation):
    i = 0
    tmp_left = left_equation
    tmp_right = right_equation
    if len(left_equation) < len(right_equation):
        left_equation, right_equation = ft_swap(left_equation, right_equation)
    if (tmp_left != left_equation and tmp_right != right_equation):
        print("<=>")
        print_equation(left_equation)
        print("=", end = " ")
        print_equation(right_equation)
    tmp_right = right_equation
    tmp_left = left_equation
    for coeff in right_equation:
        left_equation[i] += -coeff
        right_equation[i] = 0
        if len(right_equation) > 1:
            print("\n<=>")
            print_equation(left_equation)
            print("=", end = " ")
            print_equation(right_equation)
        i += 1
        tmp_right = right_equation
        tmp_left = left_equation
    print("<=>")
    print("Reduced form:", end = " ")
    print_equation(left_equation)
    print("= 0")
    return(left_equation)

def get_degree(equation):
    i = len(equation) - 1
    while i >= 0:
        if equation[i] == 0:
            i -= 1
        else:
            return(i)
    return(0)

def calc_delta(equation): #a = degree 2 b degree 1 et c degree 0
    delta = equation[1] * equation[1] - 4 * equation[2] * equation[0]
    print("\n∆ = b^2-4ac")
    print(f"∆ = {equation[1]}^2 - 4 * {equation[2]} * {equation[0]}")
    print(f"∆ = {delta}")
    return(delta)

def second_degree(equation):
    if len(equation) - 1 == 2:
        delta = calc_delta(equation)
        if delta > 0:
            print("\nDiscriminant is strictly positive, the two solutions are:")
            x1 = (-equation[1] - ft_sqrt(delta)) / (2 * equation[2])
            x2 = (-equation[1] + ft_sqrt(delta)) / (2 * equation[2])
            print(f"X1 = (-({equation[1]}) - √{delta}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x1)
            print(f"X2 = (-({equation[1]}) + √{delta}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x2)
        elif delta == 0:
            print("\nDiscriminant is null, the solution is:")
            x1 = -equation[1]/(2*equation[2])
            print(f"X1 = -({equation[1]}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x1)
        else:
            print("\nDiscriminant is negative no real solution.")
            print("\nThe two complex solutions are:")
            print("α ± β*i")
            print("α = -b / (2 * a)")
            print("β = √∆ / (2 * a)")
            print("X1 = (-b - i√∆) / (2 * a)")
            print("X2 = (-b + i√∆) / (2 * a)")
            real_part = -equation[1] / (2 * equation[2])  # α
            imag_part = ft_sqrt(ft_abs(delta)) / (2 * equation[2])  #  β
            print(f"X1 = {real_part} - {imag_part} * i")
            print(f"X2 = {real_part} + {imag_part} * i")


def solve_equation(equation):
    degree = get_degree(equation)
    if degree >= 1:
        print(f"\nPolynomial degree: {degree}")
    if len(equation) > 3:
        print("\nThe polynomial degree is stricly greater than 2, I can't solve.")
    if degree == 2:
        second_degree(equation)
    if degree == 1:
        x1 = -equation[0] / equation[1]
        print("\nThe solution is:")
        print(f"X1 = -({equation[0]}) / {equation[1]} =", end = " ")
        print_solution(x1)
    if degree == 0:
        print("All numbers are solution.") if equation[0] == 0 else print("It can't solve.")
#5 * X^0 + 4 * X^1 - 9.3 * X^2 + 2 - 5 = 1 * X^0