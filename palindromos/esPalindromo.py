palabra = input("Ingrese una palabra: ")

palabra  = palabra.lower()
palabra = palabra.replace(" ", "")

palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")

