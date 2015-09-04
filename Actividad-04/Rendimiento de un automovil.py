#encoding: UTF-8
#Hector Manuel Takami Flores
#Da una estimacion sobre el rendimiento de un automovil
mi=1.609
gal=3.78
    
def rendimientoKmL (rendimient):
    rendimient = kilometros/litros
    return rendimient

def rendimientoMiGal (rendimiento):
    rendimiento = (kilometros*mi)/(litros*gal)
    return rendimiento
    
    
def main ():
    
    kilometros = int(input("Kilometros recorridos"))
    litros = int(input("Litros de gasolina utilizados"))
    recorrido = int(input("¿Cuantos kilometros vas a recorrer?"))
    
    print("Si recorre",kilometros,"Km con",litros,"Litros de gasolina")        
    total=rendimientoKmL(rendimient)
    print( "El rendimiento en Km/L es: %f" % total) 
    total=rendimientoMiGal(rendimiento)
    print( "El rendimiento en Mi/Gal es: %f" % total)
    consejo=rendimientoKmL(rendimiento)*recorrido
    print("Para recorrer",kilometros,"Kms.,necesitas %f Litros" % consejo)
    
main()