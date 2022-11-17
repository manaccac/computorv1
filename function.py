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
    elif (equation[i] == '-' or equation[i] == '+' or equation[i] == '^' or equation[i] == '*' or equation[i] == '/' and ((equation[i + 1] >= '0' and equation[i + 1] <= '9') or equation[i + 1] == 'X' or equation[i] == 'x')) :
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


#5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0