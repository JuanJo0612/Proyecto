trabalenguas= "¡Compadre, cómpreme un coco! ¡Compadre, coco no compro!, porque el que poco coco come, poco coco compra y como yo poco coco como, poco coco compro!"


trabalenguas = trabalenguas.replace(",", "")
#print(trabalenguas)

trabalenguas = trabalenguas.replace("!", "")
#print(trabalenguas)

trabalenguas = trabalenguas.replace("¡", "")
#print(trabalenguas)

trabalenguas = trabalenguas.replace("coco", "cerdo")

listilla = trabalenguas.split(" ")

contador = []

for palabra in listilla:
    if palabra not in listilla:
        palabritas = listilla.count(palabra)
        contador.append(palabra)
        print(palabra, palabritas)
        