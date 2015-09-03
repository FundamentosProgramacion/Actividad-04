#encoding: UTF-8
#Autor: Sergio Alberto Hernandez Mendez
#Descripcion: Imprimir diametro, volumen y area, a partir del radio de una esfera

def pi(): #Define el numero pi para evitar repetirlo cada vez
    pi = 3.14159
    return pi

def calcularDiametro (radioEsfera): #Calcula el diametro de la esfera a partir de su radio
    diametroEsfera = 2 * radioEsfera
    return diametroEsfera

def calcularVolumen (radioEsfera): #Calcula el volumen de la esfera a partir del radio
    volumenEsfera = (4/3) * pi() * radioEsfera**3
    return volumenEsfera

def calcularArea (radioEsfera): #Calcula el área superficial de la esfera a partir del radio
    areaEsfera = 4 * pi() * radioEsfera**2
    return areaEsfera

def main():
    radio = eval (input ("Radio de la esfera"))
    diametro = calcularDiametro (radio)
    volumen = calcularVolumen (radio)
    area = calcularArea (radio)
    print ("Esfera con radio: ", radio, "\nDiametro: ", diametro )
    print ("Volumen: %.2f \nArea: %.2f" % (volumen, area))

main()