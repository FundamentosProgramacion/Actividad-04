#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo A01377515
#Tienda de video


#funcion que toma el numero de peliculas y asigna sus precios dependiendo de su tipo
def renta( estreno, normal ) :
    total = (estreno * 45) + (normal * 27)
    return total
    
'''
funcion principal: donde se pide el numero de peliculas que se rentan, 
se llama a la funcion y se imprimen los datos
'''
def main() :
    estreno = int( input("Peliculas de estreno"))
    normal = int( input("Peliculas normales"))
    print("Peliculas de estreno rentadas:",estreno)
    print("Peliculas normales rentadas:",normal)
    print("Total a pagar $%.2f" %renta(estreno,normal))

#Se llama a la funcion principal
main()