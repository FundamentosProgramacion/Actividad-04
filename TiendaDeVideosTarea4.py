#Encoding:UTF-8
#Autor: Paola Castillo Nacif, A01376654
#El programa mostrará el total a pagar por la renta de peliculas de estreno y normales

#Funcion Renta
def calcularRenta(numeroEstrenos,numeroNormales):
    totalPago=float((numeroEstrenos*45)+(numeroNormales*27))
    print ("Total a pagar:","$","%.2f"%totalPago)

def main():
    estrenos=int(input("Peliculas de estreno"))
    normales=int(input("Peliculas normales"))
    print("Peliculas de estrenos:",estrenos)
    print("Peliculas normales:",normales)
    calcularRenta(estrenos,normales)
main()