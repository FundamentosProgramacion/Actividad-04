#Encoding:UTF-8
#Autor: Manuel Zavala Gómez
#Tienda de videos

def main():
    numeroEstrenos= int(input("Peliculas de estreno"))
    numeroNormales= int(input("Peliculas normales"))
    
    calcularRenta(numeroEstrenos,numeroNormales)
    
def calcularRenta(numeroEstrenos,numeroNormales):
    totalPago= (numeroEstrenos * 45) + (numeroNormales*27)
    print("Peliculas de estreno rentadas:",numeroEstrenos)
    print("Peliculas normales rentadas:",numeroNormales)
    print("Total a pagar:$%.2f"%totalPago)
    return totalPago
        
main()