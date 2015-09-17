#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso, A01377349
#Description: Rendimiento de autos

def main():
    km=int(input("Kilometros recorridos"))
    gas=int(input("Litros de gasolina utilizados"))
    calcularRendimiento(km,gas)
    calcularLitros(km,gas)
    
#Funcion rendimiento
def calcularRendimiento(km,gas):
    rendimiento= km/gas
    millas= km/1.609344
    galones= gas*0.264172051
    a=millas/galones
    print("Si recorre %.0f km con %.0f litros de gasolina, "%(km,gas))
    print("El rendimiento en km/l es:%.2f"%rendimiento)
    print("El rendimiento en mi/galon es:%.02f"%a)

#Funcion litros
def calcularLitros(km,gas):
    kilo=int(input("¿Cuantos kilometros vas a recorrer?"))
    litros=kilo/(km/gas)
    print("Para recorrer %.0f kms.,necesitas %.2f"%(kilo,litros))
main()