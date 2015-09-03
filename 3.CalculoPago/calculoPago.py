#encoding: UTF-8
#Autor: Sergio Alberto Hernandez Mendez
#Descripcion: Calcula el pago semanal de un trabajador a partir de las horas y horas extras trabajadas 

def pagoNormal (horas, pagoPorHora): #Calcula la cantidad que se va a pagar por las horas "normales" trabajadas
    pago = horas * pagoPorHora
    return pago
    
def pagoExtra (horas, pagoPorHora):  #Calcula la cantidad que se va a pagar por las horas "extras" trabajadas
    pago = horas * pagoPorHora * 1.5
    return pago
    
def main():
    horasNormales = int (input ("Horas normales trabajadas") )
    horasExtras = int (input ("Horas extras trabajadas") )
    pagoHora = float (input ("Pago por hora normal") )

    pagoNorm = pagoNormal(horasNormales, pagoHora)
    pagoExt = pagoExtra(horasExtras, pagoHora)

    pagoTotal = pagoNorm + pagoExt

    print ("Horas normales: %i \nHoras extras: %i \nPago por hora: $%.2f" % (horasNormales, horasExtras, pagoHora))
    print ("Pago semanal normal: $%.2f \nPago semanal extra: $%.2f \nPago semanal total: $%.2f" % (pagoNorm, pagoExt, pagoTotal))

main()