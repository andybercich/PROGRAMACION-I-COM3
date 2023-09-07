#EJERCICIO 1
"""Create a while loop with the following characteristics: 

• The initial value of the variable x will be 0. 

• The increment value will be 1. 

• The exit condition of the loop will be greater than or equal to 30. 

• The execution must be broken when x is equal to 15. 

• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x. 

• You must skip the executions with the value of x in 4, 6 and 10. 

• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'. 

• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x. 

x = 0
while x<= 30: 
    x+=1
    if x == 15:
        print("LA EJECUCIÓN DEL BUCLE SE DETUVO CUANDO X VALÍA: " , x) 
        break
    elif x ==4 or x==6 or x==10:
        print("EL VALOR ", x ," DE X FUE SALTADO")
    else:
        print("EL VALOR DEL BUCLE ES: " , x)"""

#EJERCICIO 2
"""Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
Deje una línea en blanco para indicar que ha finalizado la entrada de líneas. 

line = input("INGRESA UNA LÍNEA PARA CAMBIARLA A MAYÚSCULA: ")
while line!=" " or line!="":
    print(line.upper())
    line = input("INGRESA UNA LÍNEA PARA CAMBIARLA A MAYÚSCULA: ")
    if line == " " or line =="":
        break
"""

#EJERCICIO 3
"""Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.

binnacle = 0
aux = input() . upper()
while aux !=" " or aux !="":
    if aux == " ":
        break
    elif "D"  in aux[0]:
        aux = aux . split(" ")
        aux[1] = float(aux[1])
        binnacle += aux[1]  
    elif "R" in aux[0]:
        aux = aux . split(" ")
        aux[1] = float(aux[1])
        binnacle -=aux[1]
        
    aux = input() . upper()
    

print("LA BITÁCORA ES: ", binnacle)"""

#EJERCICIO 4
"""Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. 
Imprimir la cantidad total de números primos ingresados. 
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos:
él mismo y el 1. 

number = int(input("INGRESE UN NÚMERO ENTERO POSITIVO: "))
divider =0
div =0
prime_numbers = 0
while number >0:
    divider =1
    div =0
    while divider<number:
        if number % divider == 0:
         div +=1     
        if div >2: 
            break
        divider +=1
        if divider == number and div <2:
            prime_numbers +=1
    number = int(input("INGRESE UN NÚMERO ENTERO POSITIVO: "))  """

print("HAS INGRESADO " , prime_numbers ," NÚMEROS PRIMOS")
#EJERCICIO 5
"""Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
que sean bisiestos y múltiplos de 10. 
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
excepto que también sea divisible por 400. 

first_year = int(input("INGRESA UN AÑO: "))
second_year = int(input("INGRESA UN AÑO MAYOR AL ANTERIOR: "))
for years in range(first_year-1,second_year, 1):
    if (years %4 ==0 or (years%100 ==0 and years %400==0)) and years%10==0:
        print(years) """


#EJERCICIO 6
"""Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
Utiliza la declaración continue para omitir los números impares.

number = 0
for number in range(1,20): 
    if number %2 !=0:
        continue
    print(number)"""

#EJERCICIO 7

"""Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
Cuando encuentres el número, usa break para salir del bucle. 

numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
number_i_want = int(input("INGRESA EL NÚMERO QUE DESEE BUSCAR EN LA LISTA: "))
x=0
for number_of_list in (numbers_list):
    if number_i_want == number_of_list:
        print("SE ENCONTRÓ EL NÚMERO EN LA LISTA CON EL ÍNDICE: ", x)
    x+=1 """
    
#EJERCICO 8
"""Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0",
utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida). 

option = int(input("INGRESA UNA OPCIÓN(1,2,3,0): "))
while option >0:
    if option ==1:
        print("ELEGISTE LA OPCION 1!!!!")
    elif option == 2:
        print("ELEGISTE LA OPCION 2!!!!")
    elif option == 3:
        print("ELEGISTE LA OPCION 3!!!!")
    elif option ==0:
        break
    else: 
        print("INGRESA UNA OPCIÓN VALIDA POR FAVOR")
    option = int(input("INGRESA UNA OPCIÓN (1,2,3,0): "))  """