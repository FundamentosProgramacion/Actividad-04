#Encoding:UTF-8
#Autor:Paola Castillo Nacif, A01376654
#Descripcion: el programa mostrara el rendimiento y los litros necesarios para recorrer una cantidad determinada de km

km=float(input("Kilometros recorridos"))
l=float(input("Litros de gasolina utilizados"))
mi=(km/1.609)
gal=(l/3.7854)

#calcular redimiento en km/l
def calcularRendimientoKML(kilometrosRecorridos, litrosUsados):
    rendimientoUno=(km/l)
    print ("Si recorre 350km con 23 litros de gasolina,","\nEl rendimiento en km/l es:","%.2f"%rendimientoUno)
    
calcularRendimientoKML(km,l)

#calcular rendimiento en mi/galon
def calcularRendimientoMIGAL(millasRecorridas, galonesUsados):
    rendimientoDos=(mi/gal)
    print("El rendimiento en mi/galon es:""%.2f"%rendimientoDos)
    
calcularRendimientoMIGAL(mi,gal)

kmr=int(input("¿Cuantos kilometros vas a recorrer?"))
rendimientoUno=(km/l)

#Calcular litros que se van a usar dados determinados km
def calcularLitros(kilometrosARecorrer,rendimientoKML):
    litrosFuturos=(kmr/rendimientoUno)
    print("Para recorrer",kmr,"kms.,necesitas","%.2f"%litrosFuturos,"litros")

calcularLitros(kmr,rendimientoUno)