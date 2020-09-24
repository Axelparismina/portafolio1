#E: Un numero entero.
#S: La cantidad de digitos que posee el numero.
#R: El numero debe ser entero positivo.
def cuentadigitos (num):
    if isinstance (num,int) and num>0:
        if 10 > num:
            return 1
        else:
            return 1 + cuentadigitos (num//10)
        
  
