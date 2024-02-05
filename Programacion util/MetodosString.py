# Ejemplo de cadena
cadena = "   Hola, mundo!   "

# Método para eliminar espacios en blanco al inicio y al final
cadena_strip = cadena.strip()
# 'Hola, mundo!'

# Método para convertir a mayúsculas
cadena_mayusculas = cadena.upper()
# '   HOLA, MUNDO!   '

# Método para convertir a minúsculas
cadena_minusculas = cadena.lower()
# '   hola, mundo!   '

# Método para reemplazar parte de una cadena
cadena_reemplazada = cadena.replace('mundo', 'Python')
# '   Hola, Python!   '

# Método para dividir una cadena en subcadenas
subcadenas = cadena.split(',')
# ['   Hola', ' mundo!   ']

# Método para unir una lista de cadenas en una sola cadena
nueva_cadena = '-'.join(['Python', 'es', 'genial'])
# 'Python-es-genial'

# Método para verificar si la cadena comienza con un determinado prefijo
empieza_con = cadena.startswith('Hola')
# True

# Método para verificar si la cadena termina con un determinado sufijo
termina_con = cadena.endswith('!')
# True

# Método para encontrar la posición de una subcadena en la cadena
posicion = cadena.find('Mundo')
# Posición de 'Mundo': 0 ,-1 si no es encontrado

# Ejemplo de cadena
cadena = "Hola, mundo!"

# Método para contar la cantidad de veces que aparece una subcadena
conteo_subcadena = cadena.count('o')
# Cantidad de 'o' en la cadena: 2

# Método para verificar si todos los caracteres son dígitos
es_digito = cadena.isdigit()
# False (hay caracteres que no son dígitos)

# Método para verificar si todos los caracteres son letras
es_letra = cadena.isalpha()
# False (hay caracteres que no son letras)

# Método para verificar si la cadena es alfanumérica (solo letras o dígitos)
es_alfanumerica = cadena.isalnum()
# False (hay caracteres que no son ni letras ni dígitos)

# Método para verificar si la cadena está en minúsculas
es_minusculas = cadena.islower()
# False (hay letras en mayúsculas)

# Método para verificar si la cadena está en mayúsculas
es_mayusculas = cadena.isupper()
# False (hay letras en minúsculas)

# Método para capitalizar la cadena (primera letra en mayúscula)
cadena_capitalizada = cadena.capitalize()
# 'Hola, mundo!'

# Método para dividir la cadena en palabras
palabras = cadena.split()
# ['Hola,', 'mundo!']

# Método para invertir el orden de los caracteres en la cadena
cadena_invertida = cadena[::-1]
# '!odnum ,aloH'

# Método para rellenar la cadena con ceros a la izquierda
cadena_rellenada = cadena.zfill(15)
# '0000Hola, mundo!'
#Numero de entrada es la cantidad de caracteres queridos por todo el string

# Método para obtener la longitud de la cadena
longitud_cadena = len(cadena)
# Longitud de la cadena: 12

