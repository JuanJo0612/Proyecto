numeros = [3, 5, 1, 8, 2, 5, 4, 20]  # Lista de números
mayor = numeros[0]  # Inicializamos mayor con el primer elemento de la lista

# Iteramos a través de la lista
for i in numeros:
    if i > mayor:  # Si encontramos un número mayor
        mayor = i  # Actualizamos el mayor

print("El número mayor es:", mayor)
