#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Rendimiento de autos

def rendimientoEnKmLit(kilometros,gasolina):
    rendimiento=kilometros/gasolina
    return rendimiento
    
def rendimientoEnMiGal(kilometros,gasolina):
    rendimiento2=(kilometros)/(gasolina*1.609344*0.264172051)
    return rendimiento2
    
def cantidadDeLitros(kilometros,rendimiento):
    litros=kilometros/rendimiento
    return litros
    
def main():
    distancia=int(input('Recorrido en kilometros'))
    litros=int(input('Consumo en litros'))
    kilometros=int(input('¿Cuantos kilometros va a recorrer?'))
    rendimiento=rendimientoEnKmLit(distancia,litros)
    rendimiento2=rendimientoEnMiGal(distancia,litros)
    gasolina=cantidadDeLitros(kilometros,rendimiento)
    print('Si recorre',distancia,'km con',litros,'litros de gasolina')
    print('Su rendimiento sera de: %.2f'%rendimiento,'km/l')
    print('Su rendimiento sera de: %.2f'%rendimiento2,'mi/gal')
    print('Para recorrer',kilometros,'km necesitara: %.2f'%gasolina,'litros')
main()

    
    