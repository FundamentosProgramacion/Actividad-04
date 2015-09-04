#encoding: UTF-8
#Hector Manuel Takami Flores
#Calcula diametro, volumen, area de un circulo. 
pi=3.15
    
def calcularDiametro (radio):
    diametro = radio*2
    return diametro

def calcularVolumen (radio):
    volumen = (((4*pi)/3)*(radio**3))
    return volumen
    
def calcularArea(radio):
    area = ((4*pi)*(radio**2))
    return area
    
def main ():
    
    radio = float(input("Radio de la esfera"))
        
    total=calcularDiametro(radio)
    print( "Diametro: %f" % total) 
    total=calcularVolumen(radio)
    print( "Volumen: %f" % total)
    total=calcularArea(radio)
    print("Area: %f" % total)
    
main()