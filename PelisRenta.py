# encoding: UTF-8   
# Autor: Humberto Serra Mendieta
# Calcula el total a pagar de rentas de peliculas

# funcion que calcula el total a pagar
def calcularRenta(pelisEstreno,pelisNormal):
    estrenos=pelisEstreno*45
    normales=pelisNormal*27
    totalPagar=estrenos+normales
    return totalPagar

# funcion principal que pide los datos de entrada
# llama a la funcion calcularRenta
# e imprime los datos de salida como el total a pagar
def main():
    pEstreno=int(input("Peliculas de estreno"))
    pNormal=int(input("Peliculas normales"))
    total=(calcularRenta(pEstreno,pNormal))#llamada de la funcion calcularRenta
    print("Numero de peliculas de estreno:",pEstreno)
    print("Numero de peliculas normales:",pNormal)
    print("Total a pagar: $ %.2f"%total)
    
main()
    
    