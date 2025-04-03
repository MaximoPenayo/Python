import random

print("BIENVENDIO AL JUEGO!")

numSecreto = random.randint(1,100)
intentosMaximos = 10
intentosRealizados = 0

while intentosRealizados < intentosMaximos:
    intento = int(input("Adivina el numero entre  1 y 100: "))
    intentosRealizados += 1

    if intento == numSecreto:
        print("-----------------------------------\n")
        print(f"Felicidades, Adivinaste el numero en {intentosRealizados} intentos.")
        print("-----------------------------------\n")
        break
    elif intento < numSecreto:
        print("-----------------------------------\n")
        print(f"El numero es mayor... \nTe quedan {intentosMaximos - intentosRealizados} intentos")
        print("-----------------------------------\n")
    else:
        print("-----------------------------------\n")
        print(f"El numero es menor... \nTe quedan {intentosMaximos-intentosRealizados} intentos")
        print("-----------------------------------\n")

if intentosRealizados == intentosMaximos:
    print("-----------------------------------\n")
    print("\tGAME OVER\t")
    print("-----------------------------------\n")
