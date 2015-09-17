#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso
#Description: Calcular Renta


#Funcion renta
def calcularRenta (noEstrenos, noNormales):
    totalPago=(noEstrenos*45)+(noNormales*27)
    return totalPago
    
    
def main():
    estrenos=int(input("Peliculas de Estreno"))
    normales=int(input("Peliculas normales"))
    total=calcularRenta(estrenos,normales)
    print("Peliculas estreno rentadas:",estrenos)
    print("Peliculas normales rentadas:",normales)
    print("Total a pagar: $%.02f" %(total))
    
main()