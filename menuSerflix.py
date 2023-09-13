movie_array = ["Star Wars", "Indiana Jones", "El Señor De Los Anillos", "Scary Movie", "Harry Potter"]
numMenu = 0
print("------------------- \n"
      "BIENVENIDO A SERFLIX \n"
      "------------------- \n")


while(numMenu != 6):
    print("Menú de opciones: \n" 
      "1. Añadir pelicula \n"
      "2. Eliminar pelicula por el nombre \n"
      "3. Buscar pelicula por nombre \n"
      "4. Mostrar todas las peliculas \n"
      "5. Buscar n peliculas \n"
      "6. Salir \n")
    numMenu = int(input("Ingrese una opción: "))
    if(numMenu == 1):
        add = int(input("Cuantas peliculas desea ingresar: "))
        print("----------------")
        for i in range(1, add+1):
            movie_array.append(input("Que pelicula desea agregar: ").title())
        print("----------------")
        continue

    elif(numMenu == 2):
        prompt = input("Ingrese la opción de la pelicula que desea eliminar: ") . title()
        print("----------------")
        ex = 0
        not_found=0
        for peli in movie_array:
            if prompt == peli:
                delete = movie_array[ex]
                del movie_array[ex]
                print(f"Se elimino la pelicula {delete}")
                print("----------------")
                continue
            else: 
                not_found+=1
            ex+=1
            if not_found == len(movie_array):
                print("Película no encontrada")

    elif(numMenu == 3):
        search_movie = (input("Ingrese el nombre de la pelicula a buscar: ").title()).strip()
        print("----------------")
        if search_movie in movie_array:
            print(search_movie,"se encuentra en la lista")
        else:
            print(search_movie,"no se encuentra en la lista")
        print("----------------")
        continue

    elif(numMenu == 4):
        print("Las pelis son: ")
        print("----------------")
        for i in range(len(movie_array)):
            print(movie_array[i])
        print("----------------")
        continue

    elif(numMenu == 5):
        start = int(input(f"¿Desde que posición desea buscar en la lista? (Del 1 al {len(movie_array)}): "))
        end = int(input(f"¿Hasta que posición desea buscar en la lista? (Del 1 al {len(movie_array)}): "))
        print("----------------")
        if start > len(movie_array) or start < 1 or end > len(movie_array) or end < 1 : 
            print("Numeros de inicio o final no validos")
            print("----------------")
            continue
        else: 
            for i in range(start,end+1):
                print(movie_array[i-1]) 
            print("----------------")
        continue

    elif(numMenu == 6):
        print("----------------")
        print("Saliendo")
        print("----------------")
        break

    else:
        print("----------------")
        print("Opción ingresada incorrecta")
        print("----------------")
        continue

