# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula el rendimiento de un auto

# Calcula el rendimiento del vehiculo
def calcularRendimientoKmL (kilometros,litros):
    rendimiento=kilometros/litros
    return rendimiento
    
    #Convierte el rendimiento de km/l a millas/galones
def calcularRendimientoMiGal (kilometros,litros):
    millas=kilometros/1.609344
    galones=litros*0.264172051
    rendimiento=millas/galones
    return rendimiento

    #Calcula los litros a usar de acuerdo al rendimiento del vehiculo    
def calcularLitrosUsar (rendimiento,kilometros):
    litros=kilometros/rendimiento
    return litros
    
def main():
    kilometros=float(input("Kilometros recorridos"))
    litros=float(input("Litros de gasolina utilizados"))
    rendimientoKmL=calcularRendimientoKmL(kilometros,litros)
    rendimientoMiGal=calcularRendimientoMiGal(kilometros,litros)
    print("Si recorres",kilometros,"km con",litros,"litros entonces,")
    print("El rendimiento en km/l es:%.2f"%rendimientoKmL)
    print("El rendimiento en mi/gal es:%.2f"%rendimientoMiGal)
    recorrerKM=float(input("Cuantos kilometros vas a recorrer"))
    litrosUsar=calcularLitrosUsar(rendimientoKmL,recorrerKM)
    print("Para recorrer",recorrerKM,"km, necesitaras %.2f"%litrosUsar," litros")
    
main()