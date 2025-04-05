registroEstudiantes = []

while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")

    opcion = input("Seleccione una Opcion: ")

    if opcion == '1':
        print("\n-------------------------------------------\n")
        nombre = input("Nombre del Estudiante: ")
        edad = int(input("Edad del Estudiante: "))
        curso = input("Curso del Estudiante: ")
        print("\n-------------------------------------------\n")

        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curso}
        registroEstudiantes.append(estudiante)
        print("Estudiante Registrado Exitosamente!")
        print("\n-------------------------------------------\n")


    elif opcion == '2':
        if registroEstudiantes:
            print("-------------------------------------------")
            print("\nRegistro de Estudiantes: \n")
            for estudiante in registroEstudiantes:
                print(f"Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]}")
                print("-------------------------------------------")

        else:
            print("\n-------------------------------------------\n")
            print("El Registro esta vacio. Registre estudiantes primero")
            print("\n-------------------------------------------\n")

    elif opcion == '3':
        print("\n-------------------------------------------\n")
        print("\tFinalizando Programa...")
        print("\n-------------------------------------------\n")
        break
    else:
        print("Opcion Invalida... Intente de Nuevo\n")