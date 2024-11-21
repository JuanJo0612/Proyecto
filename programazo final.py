class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0] == "[" and cadena[-1] == "]"):
            print("Cadena no valida")
            return(None)
        cadena = cadena[1:-1]
        sfilas = cadena.split(";")
        self.nrows = len(sfilas)
        ncols = 0
        Filas = []
        for s in sfilas:
            filastr = s.split(" ")
            if ncols == 0:
                ncols = len(filastr)
            elif ncols != len(filastr):
                print("error por número de filas")
                return(None)
            fila_float = []
            for x in filastr:
                fila_float.append(float(x))
            Filas.append(fila_float)
            ncols = len(fila_float)
        self.ncols = ncols
        self.matriz = Filas.copy()

    def sumar(self, otra_matriz):
        # Verificar que las dimensiones de ambas matrices sean iguales
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

# Matriz proporcionada por el usuario (M)
M = Matriz("[3 5 2;1 4 -8;-3 1 4]")

# Otra matriz para realizar la suma
B = Matriz("[1 2 3;4 5 6;7 8 9]")

# Sumar las dos matrices usando el nuevo método `sumar`
C = M.sumar(B)

# Si la suma fue exitosa, puedes acceder a la matriz resultante
if C:
    # C es la nueva matriz resultante de la suma
    print(C.matriz)  # Aquí se imprime la matriz resultante directamente
