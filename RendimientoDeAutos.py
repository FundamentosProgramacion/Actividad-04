#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo A01377515
#Rendimiento de autos

#Funcion para calcular rendimiento en km/l
def renKm(km,lt) :
    renKm = km/lt
    return renKm

#Funcion para calculaar rendimiento en millas/galon
def renMi(km,lt) :
    renMi = ( (km/1.609344)/(lt*0.264172051) )
    return renMi

#Funcion que imprime litros necesarios segun los kilometros
def rango(kmARecorrer,ren) :
    rango = kmARecorrer/ren
    return rango


#Funcion principal, donde se leen e imprimen valores
def main() :
    km = int( input("Kilometros recorridos"))
    lt = int( input("Litros de gasolina utilizados"))
    print("Si recorre %i km con %i litros de gasolina," %(km, lt))
    print("El rendimiento en km/l es: %.2f" %renKm(km,lt))
    print("El rendimiento en mi/galon es: %.2f" %renMi(km,lt))
    ren = float(renKm(km,lt))
    kmARecorrer = int( input("Cuantos kilometros vas a recorrer?"))
    print("Para recorrer %i km., necesitas %.2f litros" %(kmARecorrer, rango(kmARecorrer,ren)) )



#Llamada a la funcion principal
main()