#encoding: UTF-8
# Autor: Jorge Daniel Juárez Ruiz, A01376425
#Descripción: Calcular el volumen, área y diametro de una esfera a partir de su radio

pi=3.14
def calcularVolumen(radio):
    v=4/3*(pi)*(radio)**3
    return v
   
def calcularDiametro(radio):    
      d=radio*2
      return d
      
def calcularArea(radio):
    a=pi*(radio)**2
    return a


def main():
    r=int(input("Radio"))
    v=calcularVolumen(r)
    d=calcularDiametro(r)
    a=calcularArea(r)
    print ("Esfera con radio:", r)
    print ("Diametro:",d)
    print ("Volumen: %.2f" %v)
    print ("Area: %.2f"   %a)
    
main()    
  
    