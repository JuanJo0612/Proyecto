
# Definir el procedimiento F
def F(y, z):
    return -2*z + 3*y

# Definir el procedimiento G
def G(y, z):
    return -2 * y+z

# Llamar al procedimiento F con los valores 2 y -4
result_F = F(-5, 1)

# Usar el resultado de F como entrada para G junto con el valor -2
result_G = G(-4, 2)

ans = result_F + result_G


# Mostrar el resultado
print(ans)
