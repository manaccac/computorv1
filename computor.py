import sys
import re
import function as function

if len(sys.argv) != 2:
    print("Please provide an equation as a command line argument")
    sys.exit(1)

equation = sys.argv[1]
tmp = equation

equation = function.sytax(equation)
if (equation == -1):
    sys.exit()
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



#5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
#5*x^0+4*x+-9.3*x^2=1*x^0		| -1*x^0
#-9.3*x^2+4*x+4*x^0=0	

#https://www.mathepower.com/fr/equationsdeseconddegree.php

#https://fr.wikipedia.org/wiki/%C3%89quation_du_second_degr%C3%A9
#https://www.jeuxmaths.fr/cours/equations-premier-degre.php#:~:text=On%20appelle%20%C3%A9quation%20du%20premier,inconnue%20admet%20une%20unique%20solution.