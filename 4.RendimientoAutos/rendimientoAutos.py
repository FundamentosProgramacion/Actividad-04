#encoding: UTF-8
#Autor: Sergio Alberto Hernández Méndez
#Descripcion: Calcula el rendimiento de km por litro de un auto y los litros necesiarios para recorrer ciertos kilómetros

def calcularRendimiento(distancia, gas): #Calcula el rendimiento utilizando la distancia y la cantidad de gasolina
    rendimiento = distancia /gas
    return rendimiento

def calcularGasNecesaria (distanciaPorRecorrer, rendimiento): #Calcula la cantidad de gasolina necesaria para completar un viaje de cierta distancia
    gasNecesaria = distanciaPorRecorrer / rendimiento
    return gasNecesaria

def main():
    kmRecorridos = int (input ("Kilómetros recorridos"))
    litrosGas = int (input ("Litros de gasolina utilizados"))
    miRecorridas = kmRecorridos / 1.609344
    galonesGas = litrosGas * 0.264172051
    
    rendimientoKmL = calcularRendimiento (kmRecorridos, litrosGas)
    rendimientoMiGal = calcularRendimiento (miRecorridas, galonesGas)
    
    print ("Si recorre %i km con %i litros de gasolina, \nEl rendimiento en km/l es: %.2f \nEl rendimiento en mi/galón es: %.2f" % (kmRecorridos, litrosGas, rendimientoKmL, rendimientoMiGal))

    kmPorRecorrer = int (input ("¿Cuántos kilómetros vas a recorrer?"))
    litrosNecesarios = calcularGasNecesaria (kmPorRecorrer, rendimientoKmL)
    print ("Para recorrer %i kms, necesitas %.2f litros" % (kmPorRecorrer, litrosNecesarios))
    
main()