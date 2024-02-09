def paginas_libro(libros:list) -> int:
    if len(libros)==0: #Caso base
        return 0
    else:
        return libros[0]+paginas_libro(libros[1:])
    #Suma la primera posicion y divide los demas con el 1:


def paginas(libros):
    total=0
    for libro in libros: 
        total+=libro
    return total
    

hola=[2,3,4,5]
print(paginas_libro(hola))

print(paginas(hola))

def cuenta(numero):
    if numero < 0 or numero==0:
        return 0
    else:
        print(numero) #caso desde donde restara
        numero-=1
        cuenta(numero)

print(cuenta(10))    