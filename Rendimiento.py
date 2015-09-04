# encoding UTF-8 
# Autor: Mauricio Medrano Castro, A01272273 
# Calcular el rendimiento de un auto 

def rendimientoAutoEnKm(kmRecorridos,litrosUtilizados):  #Esto calcula los km por litro que gasta 
    
    recorridoKm_litros = kmRecorridos / litrosUtilizados 
    
    return recorridoKm_litros 
    
def rendimientoAutoEnMillas(kmRecorridos, litrosUtilizados): #Esto calcula las millas por galon que gasta 
    
    unaMilla = 1.609344 
    
    unGalon = 0.264172051
         
    recorridoMillas_Galones = ((kmRecorridos/litrosUtilizados) / unaMilla) / unGalon
    
    return recorridoMillas_Galones
    
def cuantosKmRecorreran(cuantosKm): #Esto calcula lo que necesitas de litros para llegar a cierto kilometraje 
    
    litrosPorKm = 0.06572
    
    litrosNecesitados = cuantosKm * litrosPorKm
    
    return litrosNecesitados
    
def main(): #funcion principal 
    
    kmRecorridos = int(input("Kilometros recorridos")) 
    
    litrosUtilizados = int(input("Litros de gasolina utilizados")) 
    
    rendimientoDelAutoEnKm = rendimientoAutoEnKm(kmRecorridos,litrosUtilizados) 
    
    rendimientoDelAutoEnMi = rendimientoAutoEnMillas(kmRecorridos, litrosUtilizados)
    
    print ( "Si recorre", kmRecorridos, "km", "con", litrosUtilizados, "litros de gasolina,") 
    
    print ( "El rendimiento en km/1 es:", "%.2f" % rendimientoDelAutoEnKm) 
    
    print ("El rendimiento en mi/ga es:", "%.2f" % rendimientoDelAutoEnMi)
    
    cuantosKm = int(input("Cuantos kilometros vas a recorrer?"))
    
    litrosQueSeNecesitan = cuantosKmRecorreran(cuantosKm) 
    
    print ("Para", cuantosKm, "kms., necesitas","%.2f" % litrosQueSeNecesitan, "litros")
main()

