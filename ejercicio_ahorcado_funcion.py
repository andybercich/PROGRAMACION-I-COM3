import random
"""Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al
azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por
letra. El jugador tiene un número limitado de intentos antes de perder el juego.
"""
print("BIENVENIDO AL AHORCADO DE PYTHON DE ANDRÉS, TIENES 5 INTENTOS PARA ERRAR, TEN EN CUENTA QUE UNA LETRA REPETIDA ES UN ERROR")


#CREO FUNCIÓN PARA LLAMARLA EN UN BUCLE MÁS ABAJO DEPENDIENDO QUE NÚMERO SE INGRESE COMO ARGUMENTO ES LA PALABRA QUE TOCA
def ahorcado(num):
    #CREE UNA LISTA CON LAS PALABRAS COMPLETAS PARA LUEGO COMPROBAR SI LAS LETRAS ESTÁN EN DICHAS PALABRAS, Y LUEGO UNA CON LAS PALABRAS INCOMPLETAS, PARA IR MOSTRANDO COMO SE VAN COLOCANDO LAS LETRAS Y UNA LISTA PARA IR SUMANDO LAS LETRAS YA INGRESADAS
    list_words = ["DINOSAURIO", "AHORCADO", "AUTOMOVIL", "PROGRAMADOR","ASTUCIA","CORAZON","SILLON","BIBLIOTECA","ESTUFA","ASTRONAUTA","VENTILADOR","VIDRIERA","AVERAGE"]
    aux = list(len(list_words[num]) * "_")
    attempts = 0
    letters_entry = []
    #DEPENDIENDO QUE NÚMERO SE TIENE, ES LA PALABRA INCOMPLETA QUE SE TOMA DE LA LISTA
    #MIENTRAS LOS INTENTOS FALLIDOS SEAN MENORES A 5 Y YA NO HAYAN MÁS GUIONES EN LA VARIABLES AUX ( O SEA QUE SE HAYAN DESCUBIERTO TODAS LAS LETRAS) SE REALIZAEÁ EL SIGUIENTE BUCLE
    while attempts!=5 and "_" in aux:
        count = 0
        print("LETRAS INGRESADAS")
        for let in letters_entry:
            print(let, end=" ")
        print(" ")
        for letter in aux:
            print(letter, end= " ")
        print(" ")
        in_letter = input("INGRESA UNA LETRA, O UNA PALABRA SI DESEAS ARRIEGAR: ") . upper()
        #ESTE IF VE CUANTAS LETRAS SE INGRESARON, SI SE INGRESARON MÁS DE DOS, SIGNIFICA QUE SE QUIERE ARRIESGAR, ENTONCES COMPARA DIRECTAMENTE LA PALABRA INGRESADA CON LA PALABRA COMPLETA DE LA PRIMERA LISTA, SINO COMPARA LA LETRA INGRESADA CON LAS QUE HAY EN LA LISTA DE PALABRAS COMPUESTAS.
        if len(in_letter) <2: 
            #ESTE IF COMPRUEBA SI LA LETRA YA SE INGRESÓ ANTERIORMENTE Y SI ESTABA EN LA PALABRA SE ESCRIBE EL MENSAJE DE ESTA LETRA YA SE INGRESO, SI NO SE INGRESÓ Y ESTA EN LA LISTA DE PALABRAS, SE REEMPLAZA EL GUIÓN POR LA LETRA INGRESADA, Y SI LA LLETRA NO ESTÁ EN LA PALABRA SE SUMÁ UN INTENTO
            if in_letter not in letters_entry:
                letters_entry.append(in_letter)
            if in_letter not in aux and in_letter in list_words[num]:
                for letters in list_words[num]:
                    if in_letter == letters:
                        print(aux[count],"ESTA ES LA LETRA")
                        aux[count] = in_letter
                    count+=1
                print("ACERTASTE UNA LETRA!!")
            elif in_letter in aux:
                print("ESA LETRA YA ESTÁ INGRESADA")
                attempts +=1
            else:
                print("NO SE ENCUENTRA ESA LETRA EN LA PALABRA :(")
                attempts +=1
        else:
            #AQUÍ SE COMPARA DIRECTAMENTE LAS LETRAS INGRESADAS CON LA PALABRA COMPLETA UNA VEZ QUE SE INGRESARON MÁS DE DOS LETRAS, Y SI ES CORRECTA LANZA UN MENSAJE DE QUE SE ACERTÓ LA LETRA, Y SINO QUE PERDIÓ TODO EL JUEGO DIRECTAMENTE
            if in_letter == list_words[num]:
                print("FELICIDADES ACERTASTE LA PALABRA: "+ in_letter)
                break
            else:
                print("LO SIENTO, NO ACERTASTE LA PALABRA, LA CUAL ERA: " , list_words[num])
                break
        #ESTE IF SIRVE PARA UNA VEZ QUE SE SALIÓ DEL BUCLE Y CONSECUENTEMENTE SE LE ACABARON LOS INTENTOS PARA ERRAR O SI YA NO HAY MÁS GUIONES EN LAS PALABRAS, MUESTRA UN MENSAJE PARA CADA UNA DE LAS SITUACIONES Y A CONTINUACIÓN LA PALABRA COMPLETA
        if attempts == 5 :
            print("HAS PERDIDO TODOS LOS INTENTOS LO SIENTO :( : " ,list_words[number_word])
        elif aux.count("_")==0 :
                print("ADIVINASTE LA PALABRA!! :)")
                for a in aux:
                    print(a, end=" ")
                    
                    
                    
#MAIN
                         
                    
            
print(" ")
#CREO UNA LISTA DE NUMÉROS QUE SE GENERAN AL AZAR, ASI NO SE REPITEN PALABRAS, Y DEBAJO UNA VARIABLE DE OPCIÓN, PARA ENTRAR O NO AL BUCLE. Y LA VARIABLE LA USÓ PARA COMPROBAR SI YA SE MOSTRARÓN TODAS LAS PALABRAS
list_numbers = []
variable =0
option = int(input("INGRESA 1 SI DESEAS JUGAR A MI JUEGO AHORCADO, INGRESA 0 PARA SALIR: "))
number_word = random.randint(0,12)
while option != 0 and option ==1 and variable != 13:
    while number_word in list_numbers:
        number_word = random.randint(0,12)
    list_numbers.append(number_word)
    variable +=1
    ahorcado(number_word)
    if variable < 5:
        option = int(input("SI DESEAS IR POR OTRA PALABRA INGRESA 1, SINO INGRESA 0: "))
    number_word = random.randint(0,12)
#Y ESTE IF LO USÓ PARA COMPROBAR SI SE JUGARON TODAS LAS PALABRAS, O NO
if variable== 5: 
    print("YA JUGASTE CON TODAS LAS PALABRAS!!! GRACIAS POR JUGAR")
else:
    print("GRACIAS POR JUGAR")