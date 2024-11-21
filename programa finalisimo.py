class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0] == "[" and cadena[-1] == "]"):
            return None
        
        cadena = cadena[1:-1]  # Eliminar los corchetes externos
        sfilas = cadena.split(";")  # Dividir las filas usando el separador ';'
        self.nrows = len(sfilas)
        ncols = 0
        Filas = []
        for w in sfilas:
            filastr = w.split(" ")
            if ncols == 0:
                ncols = len(filastr)
            elif ncols != len(filastr):
                return None  # Solo retorna None sin imprimir el mensaje
            filafloat = []
            for e in filastr:
                filafloat.append(float(e))
            Filas.append(filafloat)

        self.ncols = ncols
        self.matriz = Filas

    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-15.2f}", end=" ")
            print()

    def sumar(self, otra_matriz):

        if self.nrows != otra_matriz.nrows or self.ncols != otra_matriz.ncols:
            return None  # Solo retorna None si las dimensiones no coinciden
        
        # Crear la matriz resultante usando ciclos for
        filas_resultado = []
        for i in range(self.nrows):
            fila_resultante = []
            for j in range(self.ncols):
                fila_resultante.append(self.matriz[i][j] + otra_matriz.matriz[i][j])
            filas_resultado.append(fila_resultante)
        
        # Convertir la matriz resultante en cadena para crear una nueva instancia de Matriz
        resultado_str = ""
        for fila in filas_resultado:
            # Convertir cada número a string con str(x) y luego unirlos con un espacio
            fila_str = " ".join(str(x) for x in fila)
            resultado_str += fila_str + ";"
        
        # Eliminar el último ';' extra
        resultado_str = resultado_str.rstrip(";")
        
        # Crear la nueva matriz con el resultado de la suma
        return Matriz("[" + resultado_str + "]")

# 
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

# Sumar las dos matrices usando el nuevo método `sumar`
print("\nSuma de M y B:")
C = M.sumar(B)
if C:
    C.imprimir()