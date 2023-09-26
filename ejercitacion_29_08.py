#EJERCICIO 1
"""Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno,
 donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
 La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación

correr = int(input("INGRESE EL CORRIMIENTO: "))
abecedario = "abcdefghijklmnñopqrsstuvwxyz"
lista_palabras_encrip = [" ", " "," "," "," "," "]
for i in range(5):
    
    mensaje = input("INGRESE EL MENSAJE: ") . lower()
    mensaje_encriptado = " "
    for letra in mensaje:
        
            if letra in abecedario :
                
                indice = abecedario.find(letra)
                indice = (indice + correr) %27
                mensaje_encriptado += abecedario[indice]
                
            else: 
                
                mensaje_encriptado += letra              
    lista_palabras_encrip[i] = mensaje_encriptado
    

for i in range(5):
    print(f" EL MENSAJE ENCRIPTADO NÚMERO {i+1} ES {lista_palabras_encrip[i]}") """
    
#EJERCICIO 2
"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total"""


numero = 1
digito = 1
pares =0
impares = 0
numero = int(input("INGRESA UN NUMERO ENTERO POSITIVO: "))

while numero > 0:
    
    while numero >0:
        digito = numero % 10
        if digito%2 == 0 and digito != 0:
            pares +=1
        elif digito%2 != 0 and digito != 0:
            impares+=1
        numero //= 10
    print(f"El número ingresado tiene {pares} números pares y {impares} impares")
    numero = int(input("INGRESA UN NUMERO ENTERO POSITIVO: "))
    pares = 0
    impares = 0



    


    


                

                
                
                
                
            


    
        
        
