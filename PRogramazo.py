# lista = [2, 5, 21, 7, 13]
# 
# contador = 0
# suma = 0
# 
# for x in lista:
#     print(x)
#     contador = contador + 1
#     suma = suma + x
# 
# media = suma/contador
# print("la media es:", media)

class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0] == "[" and cadena[-1] == "]"):
            print("error no valido")
            return None
            
        cadena = cadena[1:-1]  # Elimina los corchetes de la cadena
        sfilas = cadena.split(";")  # Divide la cadena en filas
        self.nrows = len(sfilas)  # Número de filas
        ncols = 0
        Filas = []
        
        # Procesa cada fila
        for w in sfilas:
            filastr = w.split(" ")  # Divide la fila por los espacios
            if ncols == 0:
                ncols = len(filastr)  # Establece el número de columnas
            elif ncols != len(filastr):
                print("no coincide número de columnas")
                return None
            filafloat = [float(e) for e in filastr]  # Convierte cada elemento en flotante
            Filas.append(filafloat)
        
        self.ncols = ncols  # Número de columnas
        self.matriz = Filas  # Almacena la matriz

    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-15.2f}", end=" ")
            print()

    def sumar(self, otra_matriz):
        # Verifica si las dimensiones de las matrices son iguales
        if self.nrows != otra_matriz.nrows or self.ncols != otra_matriz.ncols:
            print("Error: Las matrices deben tener las mismas dimensiones para sumarlas.")
            return None
        
        # Crea una nueva matriz para almacenar el resultado
        resultado = []
        
        # Suma los elementos correspondientes de ambas matrices
        for i in range(self.nrows):
            fila_resultado = []
            for j in range(self.ncols):
                suma = self.matriz[i][j] + otra_matriz.matriz[i][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        
        # Devuelve una nueva instancia de Matriz con la matriz resultado
        matriz_resultado = Matriz("[{}]".format(";".join([" ".join(map(str, fila)) for fila in resultado])))
        return matriz_resultado


# Ejemplo de uso:

A = Matriz("[5 8;3 9;9 10]")  # Primera matriz
B = Matriz("[1 2;4 5;6 7]")  # Segunda matriz

A.imprimir()  # Imprime la matriz A
print("\nSumando matrices...\n")

# Sumar las matrices A y B
C = A.sumar(B)

if C:
    C.imprimir()  # Imprime la matriz resultante de la suma
