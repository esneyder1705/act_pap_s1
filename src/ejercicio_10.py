contador = 0
palabra = ""

while palabra != "fin":
    palabra = input("Escribe una palabra ('fin' para terminar): ")
    if palabra != "fin":
        contador += 1

print("Se ingresaron", contador, "palabras.")
