#E: Tres numeros enteros.
#S: La sumatoria del primer numero,hasta el segundo,tomando en cuenta el rango.
#R: Los numeros deben ser enteros positivos.
def sumaRango (ini,fin,ran):
    if isinstance (ini,int)and isinstance (fin,int)and isinstance (ran,int):
        if ini>fin:
            return 0
        else:
            return ini + sumaRango (ini+ran,fin,ran)
