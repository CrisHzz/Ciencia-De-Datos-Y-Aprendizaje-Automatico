# Crear un diccionario de ejemplo
diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo'}

# Método para acceder al valor de una clave
valor = diccionario['nombre']
# Valor de 'nombre': 'Juan'

# Método para añadir una nueva clave-valor
diccionario['trabajo'] = 'Programador'
# {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo', 'trabajo': 'Programador'}

# Método para eliminar una clave y su valor
valor_eliminado = diccionario.pop('edad')
# {'nombre': 'Juan', 'ciudad': 'Ejemplo', 'trabajo': 'Programador'}, valor eliminado: 30

# Método para obtener todas las claves del diccionario
claves = diccionario.keys()
# Claves del diccionario: dict_keys(['nombre', 'ciudad', 'trabajo'])

# Método para obtener todos los valores del diccionario
valores = diccionario.values()
# Valores del diccionario: dict_values(['Juan', 'Ejemplo', 'Programador'])

# Método para obtener pares clave-valor como tuplas
items = diccionario.items()
# Pares clave-valor del diccionario: dict_items([('nombre', 'Juan'), ('ciudad', 'Ejemplo'), ('trabajo', 'Programador')])

# Método para verificar si una clave está en el diccionario
esta_la_clave = 'nombre' in diccionario
# ¿La clave 'nombre' está en el diccionario?: True

# Método para copiar el diccionario
copia_diccionario = diccionario.copy()
# {'nombre': 'Juan', 'ciudad': 'Ejemplo', 'trabajo': 'Programador'}

# Método para borrar todos los elementos del diccionario
diccionario.clear()
# {}

# Crear un diccionario de ejemplo
diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo'}

# Método para obtener el valor de una clave o un valor por defecto si la clave no existe
valor = diccionario.get('nombre')
# Valor de 'nombre': 'Juan'

# Método para obtener el valor de una clave o un valor por defecto si la clave no existe
valor_con_defecto = diccionario.get('apellido', 'N/D')
# Valor de 'apellido' (no existe): 'N/D'

# Método para eliminar y devolver el último par clave-valor insertado en el diccionario
ultimo_item_eliminado = diccionario.popitem()
# {'nombre': 'Juan', 'edad': 30}, último item eliminado: ('ciudad', 'Ejemplo')

# Método para actualizar un diccionario con otro diccionario
diccionario_nuevo = {'profesion': 'Ingeniero', 'edad': 35}
diccionario.update(diccionario_nuevo)
# {'nombre': 'Juan', 'edad': 35, 'ciudad': 'Ejemplo', 'profesion': 'Ingeniero'}

# Método para eliminar una clave y devolver su valor o un valor por defecto si la clave no existe
valor_eliminado = diccionario.pop('ciudad', 'N/D')
# {'nombre': 'Juan', 'edad': 35, 'profesion': 'Ingeniero'}, valor eliminado: 'Ejemplo'

# Método para obtener una representación legible del diccionario
cadena_diccionario = str(diccionario)
# "{'nombre': 'Juan', 'edad': 35, 'profesion': 'Ingeniero'}"

# Método para verificar si el diccionario está vacío
esta_vacio = not bool(diccionario)
# Verifica si el diccionario está vacío (True si está vacío, False si tiene elementos)

# Método para obtener la longitud del diccionario (cantidad de pares clave-valor)
longitud = len(diccionario)
# Longitud del diccionario: 3

#Clave valor a una lista ,Lo mismo con values
diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo'}
lista_claves = list(diccionario.keys())
print(lista_claves)  # Output: ['nombre', 'edad', 'ciudad']

#Lista a diccionario
claves = ['nombre', 'edad', 'ciudad']
valores = ['Juan', 30, 'Ejemplo']

diccionario = dict(zip(claves, valores))
print(diccionario)

#lista a diccionario con valores nulos
claves = ['nombre', 'edad', 'ciudad', 'profesion']

diccionario = {clave: None for clave in claves}
print(diccionario)
