#E: Un numero entero.
#S: La cantidad de ceros que tiene un numero.
#R: El numero debe ser positivo.
def contarCeros (num):
    if isinstance (num,int)and num>0:
        if num==0:
            return 1
        else:
            return contarAux (num)
def contarAux (num):
    if num%10 == 0:
        return 1 + contarAux (num//10)
    elif num%10==0 and 10>num:
        return 1
    elif num%10 != 0 and 10>num:
        return 0
    else:
        return contarAux (num//10)
    
    
        
