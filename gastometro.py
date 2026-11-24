import json


def guardar_gastos(gastos):
    with open("gastos.json", "w", encoding="utf-8") as gastosarchivo:
        json.dump(gastos, gastosarchivo, indent=4, ensure_ascii=False)

def cargar_gastos():
    try:
        with open("gastos.json", "r", encoding="utf-8") as gastosarchivo:
            return json.load(gastosarchivo)
    except FileNotFoundError:
        gastos = []
        return gastos

gastos = cargar_gastos()

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
    if (len(gastos) == 0):
        return "No hay gastos registrados."
    else:
        suma = sum(g["monto"] for g in gastos)
        gasto_mayor = max(g["monto"] for g in gastos)
        promedio = suma / len(gastos)
        return f"Suma de los gastos: {suma:.2f}\nGasto mayor: {gasto_mayor:.2f}\nPromedio de los gastos: {promedio:.2f}"

def eliminar_gastos(gastos):
    if (len(gastos) == 0):
        return "No hay gastos registrados."
    else:
        print("Gastos registrados: ")
        for indice, gasto in enumerate(gastos):
            print(f"[{indice}] - ${gasto["monto"]} - {gasto["razon"]}")
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
            guardar_gastos(gastos)
        elif opcion == 2:
            resultado2 = resumen_gastos(gastos)
            print(resultado2)
        elif opcion == 3:
            resultado3 = eliminar_gastos(gastos)
            print(resultado3)
            guardar_gastos(gastos)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Seleccione una opcion dentro del rango.")
    except ValueError:
        print("Seleccione una opcion valida.")