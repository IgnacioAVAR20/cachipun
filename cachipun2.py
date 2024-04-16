import random

eleccion = input("Ingrese elección (piedra, papel o tijera): ")

if eleccion == "piedra":
    computadora = random.choice(["papel", "tijera"])
elif eleccion == "papel":
    computadora = random.choice(["piedra", "tijera"])
elif eleccion == "tijera":
    computadora = random.choice(["papel", "piedra"])
else:
    print("Elección inválida. Debe ser piedra, papel o tijera.")
    exit()

print("Tú jugaste:", eleccion)
print("Elección de la computadora:", computadora)

if eleccion == computadora:
    print("Empate!")
elif (eleccion == "piedra" and computadora == "tijera"):
    print("ganaste!")
elif (eleccion == "papel" and computadora == "piedra"):
    print("ganaste!")
elif (eleccion == "tijera" and computadora == "papel"):
    print("Ganaste!")
else:
    print("Perdiste! Vuelve a intentarlo!")