def invertir_cadena(cadena):
    # Caso base: cuando la cadena está vacía, termina la recursión
    if not cadena:
        return ""
    else:
        # Imprime el último carácter y llama recursivamente con el resto de la cadena
        print(cadena[-1],end="") 

        """El argumento end= en la función print
        se utiliza para evitar que se añada un salto de línea después 
        de imprimir cada carácter."""

        return invertir_cadena(cadena[:-1]) #Aqui se imprime cadena sin el ultimo

cadena_invertida = invertir_cadena("hola")
print(cadena_invertida)


word="Hablas mucho"
palabrainvertida=word[::-1]
print(palabrainvertida)