#Encoding:UTF-8
#Autor:Paola Castillo Nacif, A01376654
#Descripcion: El programa mostrara el pago tanto de horas normales como extras, asi como el total de la semana de un trabajador

horasn=int(input("Horas normales trabajadas"))
horase=int(input("Horas extras trabajadas"))
pagon=float(input("Pago por hora normal"))
pagohextra=((pagon*0.50)+(pagon))
print("Horas normales:",horasn)
print("Horas extras:",horase)
print("Pago por hora:","$","%.2f"%pagon)

def calcularPagoSNormal(tiempoNTrabajado,pagoNormal):
    pagosn=(horasn*pagon)
    print("Pago semanal normal:","$","%.2f"%pagosn)
    
calcularPagoSNormal(horasn,pagon)

def calcularPagoSExtra(tiempoEtrabajado,pagoExtra):
    pagosextra=(horase*pagohextra)
    print("Pago semanal extra:","$","%.2f"%pagosextra)

calcularPagoSExtra(horase,pagohextra)

pagosn=(horasn*pagon)
pagose=(horase*pagohextra)

def calcularPagoSTotal(PagoSemNormal,PagoExtraSem):
    pagostotal=(pagosn+pagose)
    print("Pago semanal total:","$","%.2f"%pagostotal)
    
calcularPagoSTotal(pagosn,pagose)
    