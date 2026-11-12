gastos = []
while True:
    try:
        opcion = int(input("Que desea realizar?\n1. Agregar gasto \n2. Ver resumen de gastos \n3. Salir\n"))
        if opcion == 1:
            try:
                monto_gasto = float(input("Ingrese el monto del gasto: \n"))
                if monto_gasto > 0:
                    gastos.append(monto_gasto)
                else:
                    print("Escriba un monto valido.")
            except ValueError:
                print("Escriba un monto valido.")
        elif opcion == 2:
            suma = 0
            gasto_mayor = 0
            if (len(gastos) == 0):
                print("No hay gastos registrados.")
            else:
                for gasto in gastos:
                    suma += gasto
                    if gasto > gasto_mayor:
                        gasto_mayor = gasto
                print(f"Suma de los gastos: {suma}")
                print(f"Gasto mayor: {gasto_mayor}")
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Seleccione una opcion dentro del rango.")
    except ValueError:
        print("Seleccione una opcion valida.")