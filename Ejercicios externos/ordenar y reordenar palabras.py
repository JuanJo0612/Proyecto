cad1 = "hola"
cad2 = "hello"
cad3 = "tangamandapio"

for r in cad2:
    print(r)
    
for r in cad1:
    print(r)
#ejemplo para sacar letras de las palabras

print(cad3[-1])

print(cad3[3:9])

print(cad3[3:9:2])


print(cad3[16: : -1])
print(cad3[: : -1])

#esto para dar a las letras

contador = 0

for r in cad3:
     print(r)
     contador = contador + 1
     
print(contador)
#para decir cuantas letras tiene la palabra