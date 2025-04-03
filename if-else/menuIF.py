print("Seleccione una opcion\n")
print("1-Suma\n2-Resta")
opcion = input("Seleccion: ")
opcion = int(opcion)

if opcion == 1:
    print("Has Seleccionado la suma")
    n1 = input("\nIngresa tu primer numero: ")
    n2 = input("\nIngresa tu segundo numero: ")
    suma = int(n1) + int(n2)
    print("\nEl Resultado de la Suma es: ",suma)
    exit


if opcion == 2:
    print("Has Seleccionado la resta")
    n1 = input("\nIngresa tu primer numero: ")
    n2 = input("\nIngresa tu segundo numero: ")
    resta = int(n1) - int(n2)
    print("\nEl Resultado de la resta es: ",resta)
else:
    if opcion != 1:
        print("Opcion Invalida")
        exit

    
