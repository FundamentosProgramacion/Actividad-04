#encoding: UTF-8
#Autor: Ernesto Cruz López A01169052
#Determinar la paga total de una personsa dependiendo de las horas normales y extras.

#Funcion principal
def main():
    horaNormal= int(input("Horas normales trabajadas"))
    horaExtra= int(input("Horas extra trabajadas"))
    pagoHora= int(input("Pago por hora"))
    horasNormales= calcularHorasNormales(horaNormal,pagoHora)
    horasExtras= calcularHorasExtras(pagoHora,horaExtra)
    horasTotales= calcularTotalDeHoras(horaNormal,pagoHora,horaExtra)
    print("Horas normales:", horaNormal)
    print("Horas extras:", horaExtra)
    print("Pago por hora:$%.02f" % pagoHora)
    print("Pago semanal normal:$%.02f" % horasNormales)
    print("Pago semanal extra:$%.02f" % horasExtras)
    print("Pago semanal total:$%.02f" % horasTotales)
 
#Funcion que calcula el pago por horas para saber que gana en una semana sin horas extra 
def calcularHorasNormales (horaNormal,pagoHora):
    hNormal= horaNormal*pagoHora
    return hNormal
    
#Funcion que calcula el pago por horas extra para saber el dinero adicional que se gana.
def calcularHorasExtras(pagoHora,horaExtra):
    hExtra= (((pagoHora*.5)+(pagoHora))*(horaExtra))
    return hExtra
 
#Funcion que suma de las dos funciones anteriores para saber el total de las ganacias en una semana.       
def calcularTotalDeHoras(horaNormal,pagoHora,horaExtra):
    totalHoras= calcularHorasNormales(horaNormal,pagoHora)+calcularHorasExtras(pagoHora,horaExtra)
    return totalHoras
    
main()    
          
    
 