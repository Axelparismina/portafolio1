#E: Dos numeros enteros.
#S: La division entero del primero entre el segundo.
#R: Ambos numeros deben ser enteros positivos.
def dividirRecursivo (divisor,dividendo):
    if isinstance (divisor,int)and isinstance (dividendo,int):
        if dividendo==0:
            print ("Error al dividir entre cero")
        elif dividendo==divisor:
            return 1
        elif divisor>dividendo:
            return 0
        else:
            return 1 + dividirRecursivo (divisor-dividendo,dividendo)
        
