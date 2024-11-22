lista = [2, 5, 21, 7, 13]

contador = 0
suma = 0

for x in lista:
    print(x)
    contador = contador + 1
    suma = suma + x

media = suma/contador
print("la media es", media)

# hallamos la media



def is_even(i):
    """
    input: i, a positive int
    returns True if i is even, otherwise False
    """
    
    print("inside is_even")
    return i%2 == 0

is_even(3)

#esto para más adelante

def media(lista):
    """
    input: una lista de numeros
    Calcula la media de los numeros de la lista
    """
    contador = 0
    suma = 0

    for x in lista:
        print(x)
        contador = contador + 1
        suma = suma + x

    media = suma/contador
    print("la media es:", media)
#no corre nada

    return media
    #este para pasar directamente al resultado
    
    