class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0] == "[" and cadena[-1] == "]"):
            return None
        
        cadena = cadena[1:-1]  
        sfilas = cadena.split(";")  
        self.nrows = len(sfilas)
        ncols = 0
        Filas = []
        for w in sfilas:
            filastr = w.split(" ")
            if ncols == 0:
                ncols = len(filastr)
            elif ncols != len(filastr):
                return None  
            filafloat = []
            for e in filastr:
                filafloat.append(float(e))
            Filas.append(filafloat)

        self.ncols = ncols
        self.matriz = Filas

    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-8.2f}", end=" ")
            print()

    def sumar(self, otra_matriz):

        if self.nrows != otra_matriz.nrows or self.ncols != otra_matriz.ncols:
            return None  
        
 
        filas_resultado = []
        for i in range(self.nrows):
            fila_resultante = []
            for j in range(self.ncols):
                suma = self.matriz[i][j] + otra_matriz.matriz[i][j]  # Sumar los elementos
                fila_resultante.append(suma)
            filas_resultado.append(fila_resultante)

        # Convertir filas a formato de cadena
        resultado_ene = "["
        for fila in filas_resultado:
            resultado_ene += " ".join(str(x) for x in fila) + ";"
            
        resultado_ene = resultado_ene.rstrip(";") + "]"  # Eliminar el último punto y coma y agregar el corchete final

        return Matriz(resultado_ene)  

M = Matriz("[3 5 2;1 4 -8;-3 1 4]")


B = Matriz("[1 2 3;4 5 6;7 8 9]")

print("Matriz M:")
M.imprimir()

print("Matriz B:")
B.imprimir()

print("Suma de M y B:")
C = M.sumar(B)
if C:
    C.imprimir()
