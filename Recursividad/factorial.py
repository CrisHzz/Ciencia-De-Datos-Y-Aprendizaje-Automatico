def factorial(number:float) -> float:
    if number<0:
        return None
    elif number == 0:
        return 1
    elif number == 1:
        return 1
    else:
       return number*factorial(number-1)
    
    
     