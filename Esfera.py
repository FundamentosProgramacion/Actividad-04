# encoding UTF-8
# Autor: Mauricio Medrano Castro, A01272273
# Calcular diametro, volumen y area de una esfera

def calcularDiametro(radio): #esto calcula el diametro de la esfera
    
    diametro = radio + radio 
    
    return diametro
    
def calcularVolumen(radio): #esto calcula el volumen de la esfera 
    
    pi = 3.1416
     
    volumen = (4 * pi * (radio*radio*radio)) / 3
    
    return volumen 
    
def calcularArea (radio): #esto calcula el area de la esfera 
    
    pi = 3.1416 
    
    area = (4 * pi * (radio*radio))
    
    return area 

    
    
    
def main(): #funcion principal 
     
     radio = float(input("Radio"))
     
     diametro = calcularDiametro(radio) 
     
     volumen = calcularVolumen(radio)
     
     area = calcularArea(radio) 
  
     print ( "El radio de la esfera es: %.2f " % radio )
     
     print ("El diametro de la esfera es: %.2f" %  diametro )
     
     print ("El volumen de la esfera es: %.2f" % volumen ) 
     
     print ("El area de la esfera es: %.2f" % area )   
     
     
     
     

main()
    
    