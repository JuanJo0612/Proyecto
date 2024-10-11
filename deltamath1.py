import random

# Generar un número aleatorio entre 2 y 8
x = random.randint(3, 10)

# Si x módulo 4 es igual a 3
if x % 3 == 1:
    x = x - 1  # Restar 3 a x
else:
    x = x  + 3  # Sumar 2 a x

# Mostrar el valor de x
print(x)
