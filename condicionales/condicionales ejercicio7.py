letrita = input("Introduce una letrita tio: ")

if len(letrita) == 1:
    letra = (letrita in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if letra:
        print(letrita + " es una letra del alfabeto tio.")
    else:
        print(letrita + " no es una letra del alfabeto tio.")
else:
    print(letrita + " no es una letra del alfabeto tio.")
