#E: Un numero entero.
#S: El factorial de dicho numero.
#R: El numero debe ser positivo.
def factorial (num):
    if isinstance (num,int)and num>0:
        if num==0 or num==1:
            return 1
        else:
            return num*factorial (num-1)
