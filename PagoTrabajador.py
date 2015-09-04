# encoding UTF-8
# Autor: Mauricio Medrano 
# Calcular el pago semanal, el pago extra y el pago total 

def pagoSemanalNormal(horasNormales,pagoPorHoraNormal): #esto calcula el pago normal del trabajador
    
    pagoNormal = horasNormales * pagoPorHoraNormal
    
    return pagoNormal 
    
def pagoSemanalExtra(horasExtras,pagoPorHoraNormal): #esto calcula el pago extra del trabajador 
    
    pagoExtra = (pagoPorHoraNormal * .50 + pagoPorHoraNormal) * horasExtras
    
    return pagoExtra

    
def main(): #funcion principal 

    horasNormales = int(input("Horas trabajadas normales"))
    
    horasExtras = int(input("Horas extras trabajadas"))
    
    pagoPorHoraNormal = int(input("Pago por Hora Normal"))
    
    pagoDeLaSemanaNormal = pagoSemanalNormal(horasNormales,pagoPorHoraNormal) 
    
    pagoDeLaSemanaExtra = pagoSemanalExtra(horasExtras,pagoPorHoraNormal)
    
    pagoTotalSemanal = pagoDeLaSemanaNormal + pagoDeLaSemanaExtra 
   
    print ( "Horas normales:", horasNormales )
    
    print ( "Horas extras:" , horasExtras ) 
    
    print ( "Pago por hora normal: $ ", "%.2f" %  pagoPorHoraNormal) 
    
    print ( "Pago semanal normal: $ ", "%.2f" % pagoDeLaSemanaNormal)
    
    print ( "Pago semanal extra: $", "%.2f" % pagoDeLaSemanaExtra) 
    
    print ( "Pago semanal total: $", "%.2f" % pagoTotalSemanal) 
main()


    