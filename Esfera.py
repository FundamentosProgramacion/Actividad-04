# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula el diametro, area y volumen de una esfera a partir del radio

from math import*

# Calcula el diametro de la esfera
def calcularDiametro(radio):
    diametro=radio*2
    return diametro
    
#Calcula el area de la esfera
def calcularArea(radio):
    area=4*pi*(radio*radio)
    return area
#Calcula el volumen de la esfera
def calcularVolumen(radio):
    volumen=(4/3)*pi*(radio*radio*radio)
    return volumen

def main():
    radio=float(input("Radio de la esfera"))
    diametrO=(calcularDiametro(radio))
    areA=(calcularArea(radio))
    volumeN=(calcularVolumen(radio))
    print("Radio de la esfera: %.2f"%radio)
    print("Diametro: %.2f"%diametrO)
    print("Area: %.2f"%areA)
    print("Volumen: %.2f"%volumeN)
    
main()