# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula el pago semanal de un trabajador

# Calcula el pago semanal por horas normales
def calcularPagoNormal(pagoHora,horasNormales):
    pagoNormal=pagoHora*horasNormales
    return pagoNormal
# Calcula el pago semanal por horas extras
def calcularPagoExtra(pagoHora,horasExtras):
    pagoHoraExtra=pagoHora+(pagoHora/2)
    pagoExtra=pagoHoraExtra*horasExtras
    return pagoExtra
    
def main():
    pagoHora=float(input("Pago por hora normal"))
    horasNormales=int(input("Horas normales trabajadas"))
    horasExtra=int(input("Horas extras trabajadas"))
    pNormal=calcularPagoNormal(pagoHora,horasNormales)
    pExtra=calcularPagoExtra(pagoHora,horasExtra)
    pagoTotal=pNormal+pExtra
    print("Horas normales:",horasNormales)
    print("Horas extras:",horasExtra)
    print("Pago por hora: $%.2f"%pagoHora)
    print("Pago semanal normal: $%.2f"%pNormal)
    print("Pago semanal extra: $%.2f"%pExtra)
    print("Pago semanal total: $%.2f"%pagoTotal)
    
main()