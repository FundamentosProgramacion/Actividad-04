#encoding: UTF-8
#Autor: Sergio Alberto Hernandez Mendez
#Descripcion: Obtener el total a pagar en una tienda de videos a partir de los estrenos y las peliculas normales

def calcularRenta (numeroEstrenos, numeroNormales): #Calcula el costo total de renta 
    totalPago = numeroEstrenos * 45 + numeroNormales * 27
    return totalPago
    
def main():
    estrenos = int(input ("Peliculas de estreno"))
    normales = int(input ("Peliculas normales"))
    total = calcularRenta(estrenos, normales)
    print ("Peliculas de estreno rentadas: %i \nPeliculas normales rentadas: %i \nTotal a pagar: $%.2f" % (estrenos, normales, total))
    
main()