
lista = input("INGRESE DIA DE LA SEMANA, DIA DE FECHA/MES EN ESTE FORMATO: dia, dd/mm: ")

lista = lista .split(",") 

lista[0] = lista[0] . upper()


lista2 = lista[1]

lista2 = lista2 . split("/")

lista2[0] = int(lista2[0])

lista2[1] = int(lista2[1])


if lista2[0] <= 31 and lista2[1] <= 12:
    
    if lista[0] == "MARTES" or (lista[0] =="MIÉRCOLES" or lista[0] == "MIERCOLES"  )  or lista[0] == "LUNES":
        
        res1 = input(("¿HOY SE TOMAN PARCIALES? (SI O NO): ")) . upper()
        
        if res1 == "SI":
                
            
            alumnos_desapro = int(input("INGRESE CAUNTOS DESAPROBARON: "))
            alumnos_aprobados = int(input("INGRESE CAUNTOS APROBARON: "))
            alumnos = alumnos_aprobados+alumnos_desapro
            porcentaje_aprobados = float((alumnos_aprobados/alumnos)*100)
            print(f"EL PORCENTAJE DE LOS ALUMNOS APROBADOS ES: {porcentaje_aprobados}%")
                
        elif res1 =="NO":
            
            print("AAAAAH BUENO")
                
    elif lista[0] == "JUEVES":
        res2 = int(input("INGRESE LA CANTIDAD DE ALUMNOS PARA LA PRÁCTICA HABLADA ESTÁN PRESENTES: "))
        res3 = int(input("INGRESE LA CANTIDAD DE ALUMNOS PARA LA PRÁCTICA HABLADA HAY EN LA LISTA: "))
        porcentaje_asist = (res2/res3) *100
        if porcentaje_asist > 50:
            print("ASISTIÓ MÁS DE LA MAYORÍA")
        elif porcentaje_asist<50:
            print("ASISTIÓ MENOS DE LA MITAD DE LOS ALUMNOS")
        elif porcentaje_asist == 50:
            print("ASISTIÓ EXACTAMENTE LA MITAD")
            
    elif lista[0] == "VIERNES" and (lista2[0] == 1 and (lista2[1] == 1 or lista2[1] == 7)):
        
        print("SE INICIA UN NUEVO CICLO")
        alumnos_nuevo_ciclo = int(input("INGRESE LA CANTIDAD DE ALUMNOS: "))
        arancel = int(input("INGRESE EL ARANCEL: "))
        print("EL INGRESO TOTAL DE DINERO ES: ", (alumnos_nuevo_ciclo*arancel))       
else:
    
    print("MES O DÍA INGRESADO NO VALIDO")
        
        
    
        

    
    

    
    



    