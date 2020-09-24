#E: Un numero entero.
#S: True si es par, False si no.
#R: Solo numeros positivos.
def esPar (num):
    if isinstance (num,int)and num > 0:
        if num%2==0:
            return True
        else:
            return False
def esImpar (num):
    if isinstance (num,int)and num> 0:
        if num%2==0:
            return False
        else:
            return True

        
