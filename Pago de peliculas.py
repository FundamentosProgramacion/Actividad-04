#encoding: UTF-8
#Autor: Jorge D. Juárez Ruiz
#Descripción: Calcular el total a pagar a partir del tipo de peliculas rentdas

def calcularRenta(noEstrenos, noNormales):
    totalPago=(noEstrenos*45)+(noNormales*27)
    return totalPago

    
def main():   
    e=int(input("No. Peliculas Estreno"))
    n=int(input("No. Peliculas Normal"))
    t= calcularRenta(e,n)
    print ("Peliculas estreno rentadas:",e)
    print ("Peliculas normales rentadas:",n)
    print ("Total a pagar: $%.02f" %(t))
    
main()