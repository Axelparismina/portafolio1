"multiplicador para la funcion potencia"
def mult (num,multi):
    if multi==0:
        return 0
    else:
        return num + mult (num,multi-1)
#E: Dos numeros enteros
#S: La potencia del primer numero al segundo numero.
#R: Los numeros deben ser positivos.
def potencia (n,p):
    if p==0:
        return 1
    if p==1:
        return n
    else:
        return mult (n,potencia (n,p-1))
