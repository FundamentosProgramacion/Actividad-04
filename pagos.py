#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo A01377515
#Pagos a un trabjador

#Funcion para calcular el pago normal
def pagoNormal(hNormal,pago) :
    pagoN = hNormal * pago
    return pagoN

#Funcion para calcular el pago extra
def pagoExtra(hExtra,pago) :
    pagoE = hExtra * ( pago/2 + pago)
    return pagoE

#Funcion principal donde se leer e imprimen datos
def main() :
    hNormal = int( input("Horas normales trabajadas:"))
    hExtra = int( input("Horas extra trabajdas:"))
    pago = float( input("Pago por hora:"))
    print("Horas normales:",hNormal)
    print("Horas extras:",hExtra)
    print("Pago por hora: $%.2f" %pago)
    print("Pago semanal normal: $%.2f" %pagoNormal(hNormal,pago))
    print("Pago semanal extra: $%.2f" %pagoExtra(hExtra,pago))
    print("Pago semanal total: $%.2f" %(pagoNormal(hNormal,pago) + pagoExtra(hExtra,pago) ))

#Llamada a la funcion principal
main()