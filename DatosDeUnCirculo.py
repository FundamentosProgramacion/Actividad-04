#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo A01377515
#Datos de un circulo

#Funcion que calcula el diametro de la esfera
def diametro(radio) : 
    diametro = radio * 2
    return diametro
    
#Funcion que calcula el volumen de la esfera
def volumen(radio) :
    volumen = (4/3) * 3.1416 * (radio * radio * radio)
    return volumen
    
#Funcion que calcula el area de la esfera
def area(radio) :
    area = 3.14146 * (radio * radio) * 4
    return area
    
#Funcion principal donde se lee el valor del radio y se imprimen los resultados
def main() :
    radio = float( input("Radio de la esfera"))
    print("Esfera con radio:" ,radio)
    print("Diametro: %.1f" %diametro(radio))
    print("Volumen: %.2f" %volumen(radio))
    print("Area: %.2f" %area(radio))
   
#Llamada a la funcion principal
main()