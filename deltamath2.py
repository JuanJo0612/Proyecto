def expression1(x):
    return x < 7 and not (x == 10)

def expression2(x):
  return not (x >= 7)

x_values = [5, 6, 7, 8, 9, 10]

for x in x_values:
    print(f"Para x = {x}:")
    print(f"Expresión 1: {expression1(x)}")
    print(f"Expresión 2: {expression2(x)}")
    print()

def Mystery(a, b, c):
    return  c - b * a


ans = Mystery(-2, 1, -1)



print(ans)
