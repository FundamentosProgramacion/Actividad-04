#encoding: UTF-8
#Hector Manuel Takami Flores
#Calcula el salario en horas normales y extras de un trabajador.

    
def horasNormales (horaNormal,pagoNormal):
    hrN = horaNormal*pagoNormal
    return hrN

def horasExtra(horaExtra,pagoNormal):
    hrE = ((horaExtra*0.5)+horaExtra)*pagoNormal
    return hrE
    
def pagoSemanal(horaNormal,horaExtra,pagoNormal):
    hrT = ((((horaExtra*0.5)+horaExtra)*pagoNormal)+(horaNormal*pagoNormal))
    return hrT
    
def main ():
    
    horaNormal = int(input("Horas normales trabajadas"))
    horaExtra = int(input("Horas Extra trabajadas"))
    pagoNormal = float(input("Pago por hora normal"))
     
    print("Horas normales:",horaNormal)
    print("Horas extras:", horaExtra)
    print("Pago por hora",pagoNormal)
       
    totalNormal=horasNormales(horaNormal,pagoNormal)
    print( "Pago semanal Normal: $ %f" % totalNormal) 
    
    totalExtra=horasExtra(horaExtra,pagoNormal)
    print( "Pago semanal Extra: $ %f" % totalExtra)
    
    totalSemanal=pagoSemanal(horaNormal,horaExtra,pagoNormal)
    print( "Pago semanal total: $ %f" % totalSemanal)
      
    
main()