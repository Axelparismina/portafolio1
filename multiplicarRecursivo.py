#E: Dos numeros enteros.
#S: La multiplicacion de ambos numeros.
#R: Ambos numeros deben ser enteros positivos.
def multiplicarRecursivo (num,factor):
    if isinstance (num,int)and isinstance (factor,int):
        if factor==0:
            return 0
        else:
            return num + multiplicarRecursivo (num,factor-1)
