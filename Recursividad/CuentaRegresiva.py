def cuenta_Regresiva(numero:int) -> int:
    #Caso base
    if numero == 0:
        return 0
    else:
        # Imprime el número actual y llama recursivamente con numero-1
        print(numero)
        return cuenta_Regresiva(numero-1)


print(cuenta_Regresiva(5))