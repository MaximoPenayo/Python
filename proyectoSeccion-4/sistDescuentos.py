print("BIENVENIDO A MOSTACHOS")
consumo = input("Ingres el monto de Consumo: ")
consumo = float(consumo)

if consumo > 50 and consumo <= 100:
    descuento = consumo * 0.9
    print("Su  consumo es de: ",consumo)
    print("Se aplicara el 10%. de descuento")
    print("TOTAL A PAGAR: ",descuento)
else:
    if consumo > 100 and consumo <= 200:
        descuento = consumo * 0.8
        print("Su  consumo es de: ",consumo)
        print("Se aplicara el 20%. de descuento")
        print("TOTAL A PAGAR: ",descuento)
    else:
        if consumo > 200:
            descuento = consumo * 0.7
            print("Su  consumo es de: ",consumo)
            print("Se aplicara el 30%. de descuento")
            print("TOTAL A PAGAR: ",descuento)
        else:
            if consumo <= 50 and consumo > 0:
                print("Su  consumo es de: ",consumo)
                print("TOTAL A PAGAR: ",consumo)
            else:
                print("Consumo Invalido")

