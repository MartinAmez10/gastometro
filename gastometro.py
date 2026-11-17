gastos = []

def agregar_gasto(gastos):
    try:
        monto_gasto = float(input("Ingrese el monto del gasto: \n"))
        razon_gasto = input("Ingrese la razon del gasto: \n")
        if monto_gasto > 0:
            gastos.append({"monto": monto_gasto, "razon": razon_gasto})
            return "Agregado."
        else:
            return "Escriba un monto valido."
    except ValueError:
            return "Escriba un monto valido."

def resumen_gastos(gastos):
    suma = 0
    gasto_mayor = 0
    if (len(gastos) == 0):
        return "No hay gastos registrados."
    else:
        for gasto in gastos:
            suma += gasto["monto"]
            if gasto["monto"] > gasto_mayor:
                gasto_mayor = gasto["monto"]
        promedio = suma / len(gastos)
        return f"Suma de los gastos: {suma:.2f}\nGasto mayor: {gasto_mayor:.2f}\nPromedio de los gastos: {promedio:.2f}"

def eliminar_gastos(gastos):
    indice = 0
    if (len(gastos) == 0):
        return "No hay gastos registrados."
    else:
        print("Gastos registrados: ")
        for gasto in gastos:
            print(f"[{indice}] - ${gasto["monto"]} - {gasto["razon"]}")
            indice += 1
        try:
            gasto_eliminado = int(input("Ingrese el indice del gasto a eliminar:\n"))
            if gasto_eliminado >= 0:
                gastos.pop(gasto_eliminado)
                return "Eliminado."
            else:
                return "Indice invalido."
        except ValueError:
            return "Escriba un indice real"
        except IndexError:
            return "Escriba un indice dentro del rango de indices"

while True:
    try:
        opcion = int(input("Que desea realizar?\n1. Agregar gasto \n2. Ver resumen de gastos \n3. Eliminar gasto \n4. Salir\n"))
        if opcion == 1:
            resultado1 = agregar_gasto(gastos)
            print(resultado1)
        elif opcion == 2:
            resultado2 = resumen_gastos(gastos)
            print(resultado2)
        elif opcion == 3:
            resultado3 = eliminar_gastos(gastos)
            print(resultado3)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Seleccione una opcion dentro del rango.")
    except ValueError:
        print("Seleccione una opcion valida.")