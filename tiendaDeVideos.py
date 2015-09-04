# encoding UTF-8
# Autor: Mauricio Medrano Castro, A01272273
# Calcular el costo de la renta de peliculas de estreno y normales 


def calcularRenta(numeroEstrenos,numeroNormales): #calcula el total por pagar por las peliculas estrenadas y normales
    
    numeroEstrenos = numeroEstrenos * 45
    
    numeroNormales = numeroNormales * 27
    
    pagoTotal = numeroEstrenos + numeroNormales 
     
    return pagoTotal 
    
def main(): #funcion principal 
    
    
    
    numeroEstrenos = int(input("Peliculas de estreno"))
    
    numeroNormales = int(input("Peliculas normales"))
    
    pagoTotal = calcularRenta(numeroEstrenos,numeroNormales)
    
    print("Numero de peliculas de estreno rentadas:", numeroEstrenos)
    
    print("Numero de peliculas normales rentadas:", numeroNormales)
    
    print("Total a pagar: $","%.2f" % pagoTotal) 
    
main()
    