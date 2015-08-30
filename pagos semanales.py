#encoding: UTF-8
# Autor: Jorge Daniel Juárez Ruiz, A01376425
#Descripcion:Calcular el pago de un trabajador con horas noramles y extra 

def calcularPagoNormal(normal,pagoHora):
    n=(normal*pagoHora)
    return n

def calcularPagoExtra(extra,pagoHora):
    e=(extra*(pagoHora+(pagoHora*0.5)))
    return e
    
def pagoSemanalTotal(n,e):
    t=n+e
    return t
    
def main():
    normal=int(input("Horas normales:"))
    extra=int(input("Horas extra"))
    pagoHora=int(input("Pago por hora"))
    n=calcularPagoNormal(normal,pagoHora)
    e=calcularPagoExtra (extra,pagoHora)
    t=pagoSemanalTotal(n,e)
    print ("Horas Normales:",normal)
    print ("Horas Extra:", extra)
    print ("Pago por hora: $%.02f" %(pagoHora))
    print ("Pago Semanal normal: $%.02f" %(n))
    print ("Pago Semanal extra:  $%.02f" %(e))
    print ("Pago Semanal total:  $%.02f" %(t))
    
main()
    