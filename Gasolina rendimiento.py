#encoding: UTF-8
# Autor: Jorge Daniel Juárez Ruiz, A01376425
#Descripcion: Calcular el rendimiento de un auto y con ellos los litros de gasolina que gastará

def calcularRendimiento(km,gas):
    r=km/gas
    return r

def calcularRendimiento2(km,gas):
    r2=(km)/(gas*1.609344*0.264172051)
    return r2
    
def calcularLitros(km,r):
    l=km/r
    return l
    
def main():
    d=int(input("Kilometros recorridos"))
    l=int(input("Litros consumidos"))
    km=int(input("¿Cuantos km reocrrió?"))
    r=calcularRendimiento(d,l)
    r2=calcularRendimiento2(d,l)
    gaso=calcularLitros(km,r)
    print ("Si recorre",d,"km con",l,"litros,")
    print ("El rendimiento es %.2f" %(r), "km/l")
    print ("El rendimiento es %.2f"%(r2), "mi/gal")
    print ("Para recorrer",km,"km, se requieren %.2f" %(gaso), "litros")
    
main()