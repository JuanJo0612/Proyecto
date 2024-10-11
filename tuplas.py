def media(lista):
    """
    input: una lista de numeros
    Calcula la media de los numeros de la lista
    """
    contador = 0
    suma = 0
    

    for x in lista:
#         print(x)
        contador = contador + 1
        suma = suma + x

    media = suma/contador
    return media

# #fin
# 

listilla = [2, 5, 9, 4]
x = media(listilla)
print("La media de la lista \n", listilla, "\n es:", x)