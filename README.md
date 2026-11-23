# GASTÓMETRO

## ¿Qué es el gastómetro?
El gastómetro es un programa de consola hecho en Python para registrar, consultar y eliminar gastos. Sirve como un proyecto de práctica personal, donde trabajé funciones y características de Python que estudié previo a trabajar en este proyecto.

## ¿Qué puede hacer quien lo use?
El usuario podrá, al ejecutar el programa, realizar una de las 4 opciones presentadas en la consola:
1. Agregar gastos: Se registra el monto y la razón de un gasto, y se agrega a la lista.
2. Mostrar resumen de gastos: Consultar un resumen de los gastos registrados (si es que existen), mostrando valores de interés, como lo son el gasto más grande registrado, la suma total de los gastos y el promedio de los mismos.
3. Eliminar gastos: Eliminar un gasto, guiado por los índices mostrados en la consola.
4. Salir: Cerrar el programa.

## ¿Cómo se puede ejecutar?
El programa puede ser ejecutado al hacer debug normalmente desde tu editor de código y solo requiere de tener instalado cualquier versión de Python de 3.12 o superior (para evitar problemas con ciertos elementos del código, que pueden no ser compatibles con versiones anteriores). Alternativamente, puede ejecutarse directamente desde la terminal con el comando ```python gastometro.py```.

## ¿Dónde se guardan los gastos?
Se guardan en una lista llamada "gastos", donde cada gasto es un diccionario dentro de la lista, la cual está ligada a un archivo JSON, llamado "gastos.json". Este archivo se crea automáticamente al agregar algún gasto mediante el programa por primera vez (o si no existe el archivo al momento de agregar un gasto). Este archivo no se encuentra en el repositorio, dado que ha sido excluido con .gitignore.

## ¿Qué conceptos se usaron?
Se usaron los conceptos y funciones de Python referentes a ciclos, condicionales, listas, diccionarios, funciones y parámetros, manejo de errores y archivos JSON. 

## Historia del proyecto
- **12 de noviembre:** Funcionalidad como una lista temporal, consultando también suma total y el gasto mayor.
- **13 de noviembre:** Añadido de la función de eliminar gastos y la razón del gasto, ligada al monto del gasto.
- **16 de noviembre:** Separación del programa en funciones.
- **17 de noviembre:** Ajuste en validaciones y agregado de la función de mostrar promedio en el resumen de gastos.
- **19 de noviembre:** Incorporación del guardado y carga de la lista en un archivo JSON.