mayor = -1
edad = 0

while edad != -1:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad != -1 and edad > mayor:
        mayor = edad

print("La edad mayor ingresada fue:", mayor)
