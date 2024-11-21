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


# Función para sumar dos matrices
def sumar_matrices(A: Matriz, B: Matriz) -> Matriz:
    if A.nrows != B.nrows or A.ncols != B.ncols:
        return None  # Solo retorna None sin imprimir el mensaje
    
    filas_resultado = []
    for i in range(A.nrows):
        fila_resultado = []
        for j in range(A.ncols):
            fila_resultado.append(A.matriz[i][j] + B.matriz[i][j])
        filas_resultado.append(fila_resultado)
    
    # Convertimos la matriz de resultado a una cadena para usar el constructor
    cadena_resultado = "[" + ";".join(" ".join(str(e) for e in fila) for fila in filas_resultado) + "]"
    return Matriz(cadena_resultado)


# Matriz proporcionada por el usuario (M)
M = Matriz("[3 5 2;1 4 -8;-3 1 4]")

# Otra matriz para realizar la suma (puedes cambiar esta por cualquier otra de las mismas dimensiones)
B = Matriz("[1 2 3;4 5 6;7 8 9]")

# Imprimir la primera matriz
print("Matriz M:")
M.imprimir()

# Imprimir la segunda matriz
print("\nMatriz B:")
B.imprimir()

# Sumar las dos matrices
print("\nSuma de M y B:")
C = sumar_matrices(M, B)
if C:
    C.imprimir()
