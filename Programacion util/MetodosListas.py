#Todos los metodos de las listas en python

# Crear una lista vacía
lista = []

# Método para añadir un elemento
lista.append(4)
# [4]

# Método para extender la lista con otra lista
lista.extend([5, 6, 7])
# [4, 5, 6, 7]

# Método para insertar un elemento en una posición específica
lista.insert(1, 8)
# [4, 8, 5, 6, 7]

# Método para eliminar un elemento por valor
lista.remove(5)
# [4, 8, 6, 7]

# Método para eliminar un elemento por índice
del lista[0]
# [8, 6, 7]

# Método para eliminar el último elemento y devolverlo
elemento_eliminado = lista.pop()
# [8, 6], elemento eliminado: 7

# Método para obtener el índice de un elemento
indice = lista.index(6)
# Índice de 6: 1

# Método para contar la cantidad de veces que aparece un elemento
conteo = lista.count(8)
# Cantidad de veces que aparece 8: 1

# Método para revertir el orden de la lista
lista.reverse()
# [6, 8]

# Método para ordenar la lista
lista.sort()
# [6, 8]

# Método para copiar la lista
copia_lista = lista.copy()
# [6, 8]

# Método para borrar todos los elementos de la lista
lista.clear()
# Borra todos los elementos de la lista
# []

# Crear una lista de ejemplo
lista = [1, 2, 3, 4, 5]

# Método para acceder a un elemento por índice
elemento = lista[2]
# Accede a un elemento por índice
# Elemento en el índice 2: 3

# Método para obtener la longitud de la lista
longitud = len(lista)
# Obtiene la longitud de la lista
# Longitud de la lista: 5

# Método para comprobar si un elemento está en la lista
esta_en_la_lista = 4 in lista
# Comprueba si un elemento está en la lista
# ¿El 4 está en la lista?: True

# Método para obtener el valor máximo de la lista
maximo = max(lista)
# Obtiene el valor máximo de la lista
# Valor máximo de la lista: 5

# Método para obtener el valor mínimo de la lista
minimo = min(lista)
# Obtiene el valor mínimo de la lista
# Valor mínimo de la lista: 1

# Método para sumar todos los elementos de la lista
suma = sum(lista)
# Suma todos los elementos de la lista
# Suma de los elementos de la lista: 15

# Método para crear una lista con valores repetidos
lista_repetida = [0] * 3
# Crea una lista con valores repetidos
# [0, 0, 0]

# Método para convertir una cadena en una lista de caracteres
cadena = "Hola"
lista_de_caracteres = list(cadena)
# Convierte una cadena en una lista de caracteres
# ['H', 'o', 'l', 'a']

# Método para convertir una lista en una cadena
cadena_nueva = ''.join(lista_de_caracteres)
# Convierte una lista en una cadena
# 'Hola'
