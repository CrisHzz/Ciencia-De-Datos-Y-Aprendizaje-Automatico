def add_recursive(n:int) ->int:
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+add_recursive(n-1) #

 
papa=add_recursive(5)

print(5)  
