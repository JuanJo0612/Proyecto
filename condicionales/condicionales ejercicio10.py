letritas = input("Introduce una letrita sensual: ")

if len(letritas) == 1:
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    
    if letritas in mayusculas:
        print(letritas + " es una letra mayúscula.")
    else:
        print(letritas + " es una letra minúscula.")

#el + es para unir el texto profe.
