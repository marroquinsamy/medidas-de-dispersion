# Función que valida únicamente los datos para el cálculo de las operaciones
def validarDatos(value, index):
  while True:
    try:
      value = float(value)
      return value
    except ValueError:
      value = input(f"\nERROR: dato no soportado ({'Enter' if value == '' else value}), por favor reemplázalo; posición {index + 1} en los datos que ingresaste: ")

# Se añadió este arreglo para que sea más fácil añadir las opciones por escrito
options = [
  "Desviación media para una serie de datos",
  "Desviación media para datos agrupados en una distribución de frecuencias simple"
]

selection = ""
while selection != "#":
  print("\nBienvenido.")
  print("\nMENÚ DE OPCIONES:")
  for index, value in enumerate(options):
    print(f"{index + 1}. {value}.")
  print(f"#. Salir")
  selection = input("Elige la opción que desees ejecutar: ")
  # Validación del ingreso para seleccionar opciones del menú
  while True:
    try:
      if selection == "#":
        break
      selection = int(selection)
      while selection > len(options):
        selection = int(input(f"\nERROR: Opción inexistente. Revisa las opciones disponibles e inténtalo de nuevo: "))
      break
    except ValueError:
      selection = input(f"\nERROR: dato incorrecto ({'Enter' if selection == '' else selection}), inténtalo de nuevo: ")

  if selection == 1:
    mediaAritmetica = 0
    desviacionMedia = 0
    data = []
    print(f"\nINSTRUCCIONES DE USO:\nIngresa todos los datos separados por UN espacio, para finalizar presiona Enter.")
    preData = input("Datos: ")
    preData = preData.split(" ")
    # Validación de datos
    dataNumber = 0
    for dataNumber, value in enumerate(preData):
      data.append(validarDatos(value, dataNumber))
    dataNumber += 1
    
    # Cálculo de la media aritmética
    for index, value in enumerate(data):
      if value != "":
        mediaAritmetica += value
      else:
        break
    mediaAritmetica = mediaAritmetica / (index + 1)
    
    # Cálculo de la desviación mediaAritmetica
    for index, value in enumerate(data):
      desviacionMedia += abs(value - mediaAritmetica)
    desviacionMedia = desviacionMedia / dataNumber

    # Presentación de resultados
    print()
    print(f"Desviación media: {desviacionMedia}.")
    print(f"Media aritmética: {mediaAritmetica}.")
    print(f"Número de datos: {dataNumber}.")
    input()
else:
  print(f"\nGracias por usar mi programa :D, vuelve pronto.\nDesarrollado y escrito por Samuel Marroquín G.")
  input("Presiona Enter para salir.")