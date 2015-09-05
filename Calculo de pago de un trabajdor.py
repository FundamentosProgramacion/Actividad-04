#encoding: UTF-8
#Autor: David Salvador Ruiz Roa
#Calculo del pago de un trabajador

def Semanal(HorasN,PagoHN):
    A = HorasN*PagoHN
    return A
    
def SemanalE(HorasE,PagoHN):
    B = (HorasE*1.5)*(PagoHN)
    return B

def main():
    HorasN = int(input("Horas normales trabajadas"))
    HorasE = int(input("Horas extras trabajadas"))
    PagoHN = int(input("Pago por hora normal"))
    PagoSemN = Semanal(HorasN,PagoHN)
    PagoSemE = SemanalE(HorasE,PagoHN)
    PagoSemT = PagoSemN + PagoSemE
    
    print("Horas normales:",HorasN)
    print("Horas extras:",HorasE)
    print("Pago por hora: $",PagoHN)
    print("Pago semanal normal: $",PagoSemN)
    print("Pago semanal extra: $",PagoSemE)
    print("Pago semanal Total: $",PagoSemT)
    
main()