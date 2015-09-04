#ecoding: UTF-8
#Autor: Ernesto Cruz López A01169052
#Determina el rendimiento de un carro km/l y mi/galon, además la gasolina necesaria para ciertos km.

#Funcion principal.

def main ():
    kilometros= int(input("Kilometros recorridos"))
    litros= int(input("Litros de gasolina utilizados"))
    kmPorLitro=rendimientoKmPorLitro(kilometros,litros)
    miPorGalon=rendimientoMiPorGalon(kilometros,litros)
    print("Si recorre %ikm con %i litros de gasolina." % (kilometros,litros))
    print("El rendimiento en km/l es: %.02f" %  kmPorLitro)
    print("El rendimiento en mi/galon es: %.02f" %  miPorGalon) 
    kilometrosARecorrer= int(input("¿Cuantos kilometros vas a recorrer?"))
    fuel= gasolinaNecesaria(kilometrosARecorrer,kilometros,litros)
    print("Para recorrer %ikm; necesitas %.02f litros"  % (kilometrosARecorrer,fuel))
    
# Funcion que divide los kilometros entre horas para poder saber el prier rendimiento.
def rendimientoKmPorLitro(kilometros,litros):
    rendimiento1=kilometros/litros
    return rendimiento1

#Funcion que trae la funcio rendimientoKmPorLitro para hacer un conversion mi/galon.    
def rendimientoMiPorGalon(kilometros,litros):
    rendimiento2=(( rendimientoKmPorLitro(kilometros,litros))/(1.609344*.264172051))
    return rendimiento2

#Funcion que divide los kilometros a recorren entre la funcion rendimientoKmPorLitro para poder saber los litros necesario para cierta distancia.
def gasolinaNecesaria(kilometrosARecorrer,kilometros,litros):
    gasolina=kilometrosARecorrer/rendimientoKmPorLitro(kilometros,litros)
    return gasolina
    
main()
    