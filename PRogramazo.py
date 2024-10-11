lista = [2, 5, 21, 7, 13]

contador = 0
suma = 0

for x in lista:
    print(x)
    contador = contador + 1
    suma = suma + x

media = suma/contador
print("la media es:", media)