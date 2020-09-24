#E: Dos numeros enteros.
#S: La sumatoria del primer numero hasta el segundo.
#R: Los numeros deben ser positivos.
def sumatoria (inicio,final):
    if isinstance (inicio,int) and isinstance (final,int):
        if inicio==final:
            return final
        else:
            return inicio + sumatoria (inicio+1,final)
    
    
        
