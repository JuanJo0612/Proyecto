lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("El triángulo es válido.")
else:
    print("El triángulo no es válido.")
