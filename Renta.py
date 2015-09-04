#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Renta

def calcularRenta(numeroEstrenos, numeroNormales):
    totalPago=(numeroEstrenos*45)+(numeroNormales*27)
    return totalPago
    
def main():
    estrenos=int(input('Numero de Estrenos'))
    normales=int(input('Numero de Normales'))
    totalPago=calcularRenta(estrenos,normales)
    print('El numero de peliculas de estrenos es de ',estrenos)
    print('El numero de peliculas normales es de ',normales)
    print('El total a pagar es de: $%.02f' %totalPago)
main()


