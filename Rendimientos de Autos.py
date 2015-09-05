#encoding: UTF-8
#Autor: David Salvador Ruiz Roa
#Rendimiento de Autos

def kiloml(km,lts):
    A = km/lts
    return A
    
def millag(km,lts):
    B = km/1.609344
    C = lts*0.264172051
    D = B/C
    return D
    
def N(kml,recorre):
    E = recorre/kml
    return E

def main():
    km = int(input("kilometros recorridos"))
    lts = int(input("Litros de gasolina consumidos"))
    kml = kiloml(km,lts)
    milla = millag(km,lts)
    print("Si recorre %i km con %i litros de gasolina,"% (km,lts))
    print("El rendimiento en km/l es: %i"% (kml))
    print("El rendimiento en mi/galon es: %i"%(milla))
    recorre = int(input("¿Cuantos kilometros vas a recorrer?"))
    necesita = N(kml,recorre)
    print("Para recorrer %i kms., %i litros"%(recorre,necesita))

main()