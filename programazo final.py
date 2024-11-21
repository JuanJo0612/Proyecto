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
        if self.nrows != otra_matriz.nrows or self.ncols != otra_matriz.ncols:
            return None  
        
        filas_resultado = []
        for i in range(self.nrows):
            fila_resultante = []
            for j in range(self.ncols):
                fila_resultante.append(self.matriz[i][j] + otra_matriz.matriz[i][j])
            filas_resultado.append(fila_resultante)
        
        resultado_str = ""
        for fila in filas_resultado:
            fila_str = " ".join(str(x) for x in fila)
            resultado_str += fila_str + ";"
        
        resultado_str = resultado_str.rstrip(";")
        
        return Matriz("[" + resultado_str + "]")


