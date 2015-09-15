#Encoding:UTF-8
#Autor: Manuel Zavala Gómez
#Datos de un circulo
 
def main():

    radio=float(input("Radio de la esfera"))
    print("Esfera con radio",radio)
    calcularDiametro(radio)
    calcularVolumen(radio)
    calcularArea(radio)
    
def calcularDiametro(radio):
    diametro= radio*2
    print("Diametro:%.2f"% diametro)
    
def calcularVolumen(radio):
    volumen=(4*(3.1416)/3)*((radio)**3)
    print("Volumen:%.2f"%volumen)
    
def calcularArea(radio):
    area=(4*3.1416)*(radio**2)
    print("Area:%.2f"% area)

main()
