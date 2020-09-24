#E: Un numero entero.
#S: La multiplicatoria solo con numeros pares.
#R: El numero debe ser entero positivo.
def multipares (num):
    if isinstance (num,int) and num>0:
        if num==0:
            return 1
        elif num%2==0:
            return num*multipares (num-1)
        else:
            return multipares (num-1)
        
