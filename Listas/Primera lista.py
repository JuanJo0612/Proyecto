ListaNombres = ["Aiden", "Britnay", "Cristina", "David" , "Elvis", "Feid"]
Discos = [3, 20, 12, 8, 30, 3]
Estados = ["WA", "PA" , "NM" , "NY" , "IA" , "CO"]

Artista = {"Aiden" : 3,
           "Britney" : 20,
           "Cristina" : 12,
           "David" : 8,
           "Elvis" : 30,
           "Feid" : 3}
Artista["David"]

Artista. values()
Artista. keys()

for k in Artista:
    print(Artista[k])
#K es la letra que vamos a utilizar 

for k in Artista:
    print("El artista",k, "tiene", Artista[k], "discos")
#para unir todas las listas en una frase
