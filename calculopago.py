#Encoding:UTF-8
#Autor:Manuel Zavala Gómez
#Calculo de pago de un trabajador

def main():
    normal=int(input("Horas normales trabajadas"))
    extra=int(input("Horas extra trabajadas"))
    pago=int(input("Pago por hora normal"))
    print("Horas normales:",normal)
    print("Horas extras:",extra)
    print("Pago por hora:$%.2f"% pago) 
    calcularNormal(normal,pago)
    calcularExtra(normal,extra,pago)   
def calcularNormal(normal,pago):
    a=normal*pago
    print("Pago semanal normal:$%.2f"% a)
def calcularExtra(normal,extra,pago):
    b=(pago/2)+ pago
    c= b*extra
    d= (normal*pago)+c
    print("Pago semanal extra:$%.3f" % c)
    print("Pago semanal total:$%.2f"%d)    
main()     