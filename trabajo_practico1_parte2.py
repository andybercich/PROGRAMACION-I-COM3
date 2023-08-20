#EJERCICIO 6 
print("ESTE PROGRAMA SIRVE PARA CALCULAR LA MEDIA DE 3 NÚMEROS")
num1 = float(input("INGRESA EL PRIMER NÚMERO: ")) 
num2= float(input("INGRESA EL SEGUNDO NÚMERO: ")) 
num3= float(input("INGRESA EL TERCER NÚMERO: ")) 

print("LA MEDIA DE LOS TRES NÚMEROS DADOS ES DE: ", (num1 + num2 + num3)/3)

#EJERCICIO 7

print("ESTE PROGRAMA SIRVE PARA CALCULAR LA CANTIDAD DE HORAS Y MINUTOS CORRESPONDEN A LA CANTIDAD DE MINUTOS INGRESADOS")

minutos_ingresados = int(input("INGRESE LA CANTIDAD DE MINUTOS QUE DESEA CALCULAR: "))

horas_calculadas = int(minutos_ingresados/60)
minutos_caclulados = int(minutos_ingresados%60)
print("LA CANTIDAD DE MINUTOS INGRESADOS ES: ", "HORA: " ,horas_calculadas , "MINUTOS: ", minutos_caclulados)


#EJERCICIO 8 :
venta1 = int(input("INGRESE EL VALOR DEL PRODUCTO VENDIDO: "))
venta2 = int(input("INGRESE EL VALOR DEL PRODUCTO VENDIDO: "))
venta3 = int(input("INGRESA EL VALOR DEL PRODUCTO VENDIDO: "))
sueldo_base = 60000
venta1 = 5000*0.1
venta2 = 4000*0.1
venta3 = 8000*0.1
ventas_totales = venta1+venta2+venta3
ganancia_total = sueldo_base + ventas_totales
print("EL TOTAL QUE COBRARÁ EL EMPLEADO ES: ",ganancia_total)







