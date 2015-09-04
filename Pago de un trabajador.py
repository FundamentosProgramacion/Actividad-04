#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Pago de un trabajador

def calcularPagoNormal(normal,pHora):
    normal=normal*pHora
    return normal
    
def calcularPagoExtra(normal,pHora):
    extra=normal*pHora*0.5
    return extra
    
def calcularPagoSemanalTotal(normal,pHora):
    total=normal*pHora
    return total
    
def main():
    normal=int(input('Horas normales: '))
    extra=int(input('Horas extras: '))
    pHora=int(input('Pago por hora: '))
    normal=calcularPagoNormal(normal,pHora)
    extra=calcularPagoExtra(normal,pHora)
    total=calcularPagoSemanalTotal(normal,pHora)
    print('Las horas normales: ',normal)
    print('Las horas extras: ',extra)
    print('El pago por hora es de: $%.02f' %pHora)
    print('El pago semanal normal es de: $%.02f' %normal)
    print('El pago semanal extra es de: $%.02f' %extra)
    print('El pago semanal total es de: $%.02f' %total)
main()