#encoding: UTF-8
#Autor: David Salvador Ruiz Roa
#Tienda de videos

def calcularRenta(Estreno,Normales):
     T = ((Estreno*45) + (Normales*27))
     return T

def main():
    Estreno = int(input("Pelculas de estreno"))  #$27
    Normales = int(input("Pelculas de normales")) #$45
    Total = calcularRenta(Estreno,Normales)
    print("Peliculas de estreno Rentadas:",Estreno)
    print("Peliuclas normales rentadas:",Normales)
    print("Total a pagar: $",Total)
    

main()