"Ejercicio 1"
import random
def rat(minutes):
    option = random.randint(1,3)
    if option ==1:
        return rat(minutes+3)
    elif option == 2:
        return rat(minutes+5)
    elif option == 3:
        return minutes+7

print(f"La rata salio dentro de {rat(0)}")

"Ejercicio 2: Realizar una función recursiva que devuelva el número ingresado a la inversa en formato string: Ejemplo 2458 a 8542"

def f(n):
    s  = str(n)
    if len(s)<= 1:
        return s
    return s[-1] + f(int(s[:-1]))
print(f(2458))
    