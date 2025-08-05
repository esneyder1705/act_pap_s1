import random

secreto = random.randint(1, 10)
intento = 0

while intento != secreto:
    intento = int(input("Adivina el número (1 al 10): "))

print("¡Felicidades! Adivinaste el número.")
