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
            print("-", end = "") if i == get_degree(equation) else print("-", end = " ")
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

def sytax(equation):
  i = 0
  equation = str(equation).replace(' ', '')
  
  close = True
  egale = False
  while i != len(equation) :
    if (equation[i] >= '0' and equation[i] <= '9') :
      i += 1
      continue
    if (equation[i] == '=' and close == True and egale == False):
      i += 1
      egale = True
      continue
    elif (equation[i] == '(') :
      i += 1
      close = False
      continue
    elif ((equation[i] == '-' or equation[i] == '+' or equation[i] == '^' or equation[i] == '*' or equation[i] == '/') and i + 1 != len(equation) and ((equation[i + 1] >= '0' and equation[i + 1] <= '9') or equation[i + 1] == 'X' or equation[i] == 'x')) :
      i += 1
      continue
    elif (equation[i] == '.' and (equation[i + 1] >= '0' and equation[i + 1] <= '9')) :
      i += 1
      continue
    elif (equation[i] == 'X' or equation[i] == 'x') :
      if (i + 1 != len(equation)):
        if (equation[i + 1] == 'x' or equation[i + 1] == 'X') :
          return -1
        if (equation[i + 1] >= '0' and equation[i + 1] <= '9'):
          return -1
      i += 1
      continue
    elif (equation[i] == ')'):
      close = True
      i += 1
      continue
    else :
      print("ERROR ERROR ERROR")
      return -1
  if (close == False) :
    return -1
  return (equation)


def cut_equation(equation):
    index_coeff = []
    i = 0
    for element in equation:
        if not element == "+" and not element == "-" and not len(element) == 0:
            element = element.split("*")
            if len(element) > 2:
                exit()
            elif len(element) == 1 and element[0].lower().startswith("x"):
                element.insert(0, "1")
            if len(element) > 1:
                if element[1].lower() == 'x':
                    power = 1
                else:
                    power = element[1].lower().lstrip("x^")
            else:
                power = 0
            if equation[i - 1] == "+" or equation[i - 1] == "-":
                coeff = equation[i - 1] + element[0]
            else:
                coeff = element[0]
            if len(index_coeff) - 1 >= int(power):
                index_coeff[int(power)] += float(coeff)
            else:
                while len(index_coeff) < int(power):
                    index_coeff.insert(len(index_coeff), 0)
                index_coeff.insert(int(power), float(coeff))
        i += 1
    return(index_coeff)

def reduced_form(left_equation, right_equation):
    i = 0
    if len(left_equation) < len(right_equation):
        left_equation, right_equation = ft_swap(left_equation, right_equation)
    print("<=>", end = " ")
    print_equation(left_equation)
    print("=", end = " ")
    print_equation(right_equation)
    for coeff in right_equation:
        left_equation[i] += -coeff
        right_equation[i] = 0
        if len(right_equation) > 1:
            print("\n<=>")
            print_equation(left_equation)
            print("=")
            print_equation(right_equation)
        i += 1
    print("\nReduced form:", end = " ")
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
            print("\nDiscriminant is nul, the solution is:")
            x1 = -equation[1]/(2*equation[2])
            print(f"X1 = -({equation[1]}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x1)
        else:
            print("\nDiscriminant is negatif, the two complexes solutions are:")
            num = -equation[1]
            denom = 2 * equation[2]
            print(f"X1 = (-({equation[1]}) - i√{ft_abs(delta)}) / (2 * {equation[2]})")
            print(f"X2 = (-({equation[1]}) + i√{ft_abs(delta)}) / (2 * {equation[2]})")
            if num != 0:
                print(f"X1 = ({num} - i√{ft_abs(delta)}) / {denom}")
                print(f"X1 = ({num} + i√{ft_abs(delta)}) / {denom}")
            else:
                print(f"X1 = -i√{ft_abs(delta)} / {denom}")
                print(f"X1 = i√{ft_abs(delta)} / {denom}")

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