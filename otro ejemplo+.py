trabalenguas= "¡Compadre, cómpreme un coco! ¡Compadre, coco no compro!, porque el que poco coco come, poco coco compra y como yo poco coco como, poco coco compro!"


trabalenguas = trabalenguas.replace(",", "")
#print(trabalenguas)

trabalenguas = trabalenguas.replace("!", "")
#print(trabalenguas)

trabalenguas = trabalenguas.replace("¡", "")
#print(trabalenguas)

trabalenguas = trabalenguas.lower()

listas = trabalenguas.split(" " )
conjunto = set(listas)
lista = list(conjunto)
print(" ". join(lista))


