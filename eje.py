# Definir las expresiones booleanas
def expression1(x):
    return x < 7 and not (x == 10)

#def expression2(x):
 #   return not (x >= 7)

# Probar las expresiones con diferentes valores de x
#x_values = [5, 6, 7, 8, 9, 10]

#for x in x_values:
 #   print(f"Para x = {x}:")
  #  print(f"Expresión 1: {expression1(x)}")
    #print(f"Expresión 2: {expression2(x)}")
    #print()
# Definir el procedimiento Mystery
def Mystery(a, b, c):
    return  c - b * a

# Llamar al procedimiento con los valores dados
ans = Mystery(-2, 1, -1)


# Mostrar el resultado
print(ans)
