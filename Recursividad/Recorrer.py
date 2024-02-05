
def recorrer_matriz(matriz):

# Verifica si la matriz está vacía o es None
    if not matriz:
        return "Esta vacia"
    # Recorre cada fila en la matriz
    for fila in matriz:
        # Recorre cada elemento en la fila e imprímelo
        for elemento in fila:
            print(elemento)

    recorrer_matriz(matriz[1:])
     # Llamada recursiva con la matriz excluyendo la primera fila

matriz = [[2, 3, 4], [1, 5, 6], [4, 2, 0]]
recorrer_matriz(matriz)
