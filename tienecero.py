#E: Un número entero positivo.
#S: True si tiene cero, False si no tiene.
#R: El número tiene que ser entero y positivo.
def tienecero (num):
    if isinstance (num,int)and num >= 0:
        if num == 0:
            return True
        else:
            return tieneceroaux (num)
def tieneceroaux (num):
    if num== 0:
        return False
    elif num%10==0:
        return True
    else:
        return tieneceroaux (num//10)
