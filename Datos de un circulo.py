#encoding: UTF-8
#Autor: David Salvador Ruiz Roa
#Datos de un círculo

from math import pi

def Diametro(Radio):
    Diam = Radio*2
    return Diam

def Volumen(Radio):
    V = (((4/3)*pi)*(Radio*Radio*Radio))
    return V

def Area(Radio):
    A = 4*pi*(Radio*Radio)
    return A

def main():
    Radio = int(input("Radio de la esféra:"))
    Dia = Diametro(Radio)
    Vol = Volumen(Radio)
    Are = Area(Radio)
    print("Esfera con Radio:",Radio)
    print("Diametro:",Dia)
    print("Volumen:",Vol)
    print("Área:",Are)
    
main()