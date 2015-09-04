#encoding: UTF-8
#Autor: Ernesto Cruz López A01169052
#Determinar el total a pagar dependiendo el numero de peliculas de estreno o normales que tomes.

#Funcion principal.
def main():
    numEstreno= int(input("Peliculas estreno"))
    numNormal=int(input("Peliculas normales"))
    total = calcularRenta(numEstreno,numNormal)
    print("Peliculas de estreno rentadas:",numEstreno)
    print("Peliculas normales rentadas:",numNormal)
    print("Total a pagar:$%.02f" % total)

#Funcion que multiplica el precio de pelicus estreno y normles por el numero de peliculas y los suma para saber el total a pagar.
def calcularRenta(numEstreno,numNormal):
    totalPagar= ((numEstreno*45)+(numNormal*27))
    return totalPagar

main()
