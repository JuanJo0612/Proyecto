numero = int(input("escribid un número chaval: "))

divisible_entrecinco = (numero // 5) * 5 == numero

if divisible_entrecinco:
    print("El número", numero, "es divisible por 5 chaval.")
else:
    print("El número", numero, "no es divisible por 5 chaval.")

numero2 = int(input("escribid otro número chaval: "))

divisible_entreonce = (numero // 11) * 11 == numero

if divisible_entreonce:
    print("El número", numero, "es divisible por 11 chaval.")
else:
    print("El número", numero, "no es divisible por 11 chaval.")