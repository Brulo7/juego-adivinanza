from operator import truediv
import random


numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("En este juego debes adivinar el numero secreto.")

while not adivinado:
    numero = int(input("Introduce tu numero del 1 al 100: "))
    if numero == numero_secreto:
        print("Muy bien, adivinaste el numero >:|")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor al ingresado ;)")
    else:
        print("El numero es menor al ingresado ;)")
    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("¡Game over! No pudiste el completar el juego.")