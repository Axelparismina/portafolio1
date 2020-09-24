#E: Un numero entero.
#S: Los divisores de dicho numero.
#R: El numero debe ser entero positivo.
def divisores (num):
    if isinstance (num,int):
        return divisoresAux (num,num)
def divisoresAux (divisor,pot):
    if pot==1:
        print (pot)
    elif divisor%pot==0:
        print (pot)
        return divisoresAux (divisor,pot-1)
    else:
        return divisoresAux (divisor,pot-1)
        
        
    
