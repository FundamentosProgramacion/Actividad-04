#Encoding:UTF-8
#Autor: Paola Castillo Nacif, A01376654
#El programa mostrara el diametro, volumen y area de una esfera

radio=float(input("Radio de la esfera"))
pi=3.1416
print("Esfera con radio:",radio)

#Funcion diametro
def calcularDiametro(radioEsfera):
    diametroEsfera=(radio*2)
    print("Diametro:",diametroEsfera)
    
calcularDiametro(radio)

#Funcion volumen
def calcularVolumen(radioEsfera,constante):
    volumenEsfera=(((4/3)*pi)*(radio**3))
    print("Volumen:","%.2f"%volumenEsfera)
    
calcularVolumen(radio,pi)

#Funcion area
def calcularArea(radioEsfera,constante):
    areaEsfera=(((4)*pi)*(radio**2))
    print("Area:","%.2f"%areaEsfera)
    
calcularArea(radio,pi)
