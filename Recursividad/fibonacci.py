def fibonacci(n:int) -> int:
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2) # Necesita sumar los anteriores f(5)=f(4)+f(3)
                                              # f2=f(1)+f(0) siendo 1 y 0 sus resultados
                                              # f3=f2+f1=3              
    
papa=fibonacci(7)
print(papa)

# La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores.
# Matemáticamente, la relación de recurrencia es: F(n) = F(n-1) + F(n-2) para n >= 2.
# Los casos base son F(0) = 0 y F(1) = 1.




        
        
