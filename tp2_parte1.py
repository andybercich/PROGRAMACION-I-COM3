'''17-Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado
o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.'''

'''diaSemana = input("Ingresar un dia de la semana: ")
diaSemana=diaSemana.lower()

if(diaSemana == "lunes"):
    print("El dia ingresado es lunes. ")
elif(diaSemana == "viernes"): 
        print("El dia ingresado es viernes. ")
elif(diaSemana == "sabado" or diaSemana == "domingo"): 
            print("El dia ingresado es sabado o domingo. ")
else: 
            print("Usted no ha ingresado ni Lunes, ni viernes, ni sabadado ni domingo. ")


18-Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. 
Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más
 que las horas laborales comunes.

horasTrabajadas = float(input("Ingresar la cantidad de horas trabajadas en el mes: "))
salarioHoras = float(input("Ingresar cuanto es el salario x horas: "))

if(horasTrabajadas > 48 ):
        horasExtras = (horasTrabajadas-48)
        print(f"Usted realizo {horasExtras} horas extras. ")
        salarioExtra = (horasTrabajadas*salarioHoras)*10/100
        salarioTotal = (horasTrabajadas*salarioHoras) + salarioExtra
        print("Su salario total es de: $",salarioTotal)
else: 
        salarioTotal = horasTrabajadas*salarioHoras
        print(f"Usted ha realizado {horasTrabajadas}hs. Y su salario total es de: ${salarioTotal}")

19-Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un
descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.'''
'''precioLapiz = 60

lapices = int(input("Ingresar la cantidad de lapices: "))
if(lapices >= 1000):
        print(f"Por la cantidad que lleva tine un 7% de descuento")
        descuento = (lapices*60)*7/100
        precioFinal = (lapices*60)-descuento
        print("Lo cual su total es de: $",precioFinal)
else:
        precioFinal = (lapices*60)
        print("El precio total es de: ",precioFinal)
        
20-Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara 
si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.'''

notaUno = float(input("Ingrese su primera nota: "))
notaDos = float(input("Ingrese su segunda nota: "))
notaTres = float(input("Ingrese su tercera nota: "))
notaCuatro = float(input("Ingrese su cuarta nota: "))

promedio = (notaUno + notaDos + notaTres + notaCuatro)/4
print("Su promedio es de: ",promedio)
if(promedio >= 6):
        print("APROBADO. ")
else: 
        print("DESAPROBADO. ")