numeros = [4, 1, 2, 2, 3, 4, 4, 5]  
moda = []
maxfrecuencia = 0  


for i in range(len(numeros)):
    frecuencia = 0  


    for j in range(len(numeros)):
        if numeros[j] == numeros[i]:
            frecuencia += 1

    if frecuencia > maxfrecuencia:
        maxfrecuencia = frecuencia 
        moda = numeros[i]  

print("La moda es:", moda)
