#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso
#Description: Datos de un circulo

radio=float (input("Radio de la esfera"))
pi=3.1416
print("Esfera con radio:",radio)

#Funcion diametro
def calcularDiametro(radioEsfera):
    diametroEsfera=(radio*2)
    print("Diametro:",diametroEsfera)
    
calcularDiametro(radio)

#Funcion Volumen
def calcularVolumen(radioEsfera, constante):
    volumenEsfera=(((4/3)*pi)*(radio**3))
    print("Volumen:","%.2f"% volumenEsfera)
    
calcularVolumen(radio,pi)

#Funcion area
def calcularArea(radioEsfera,constante):
    areaEsfera=(((4)*pi)*(radio**2))
    print("Area:", "%.2f"%areaEsfera)
    
calcularArea(radio,pi)