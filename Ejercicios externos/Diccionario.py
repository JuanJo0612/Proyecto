ListaNombres = ["Aiden", "Britnay", "Cristina", "David" , "Elvis", "Feid"]
Discos = [3, 20, 12, 8, 30, 3]
Estados = ["WA", "PA" , "NM" , "NY" , "IA" , "CO"]


Artista2 = {"Aiden" : [3, "WA"],
            "Britnay" : [20, "PA"],
            "Cristina" : [12 ,  "NM"],
            "David" : [8, "NY"],
            "Elvis" : [30, "IA"],
            "Feid" : [3, "CO"]}
Artista2["Britnay"][0]
Artista2["Britnay"][1]
  
for K in Artista2:
    print("el artista", K, "tiene", Artista2[K], "discos y vive en la gran", Artista2[K])