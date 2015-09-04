#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Radio de una esfera

PI=3.14

def calcularDiametroDeUnaEsfera(radio):
    diametro=radio*2
    return(diametro)
    
def calcularVolumenDeUnaEsfera(radio):
    volumen=(4*PI*(radio**3))/3
    return(volumen)
    
def calcularAreaDeUnaEsfera(radio):
    area=(4*PI*(radio**2))
    return(area)
    
def main():
    radio=int(input('radio'))
    diametro=calcularDiametroDeUnaEsfera(radio)
    volumen=calcularVolumenDeUnaEsfera(radio)
    area=calcularAreaDeUnaEsfera(radio)
    print('El radio de la esfera es de: ',radio,'unidades')
    print('El diametro de la esfera es de: ',diametro,'unidades')
    print('El volumen de la esfera es de: %.2f'%volumen,'unidades')
    print('El area de la esfera es de: ',area,'unidades')
main()