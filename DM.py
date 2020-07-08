# Función que valida los datos únicamente para el cálculo de las operaciones
def validarDatos(value, index):
  while True:
    try:
      # Esto intenta convertir los datos ingresados a números con punto decimal, si se puede hacer regresa el dato y sale del ciclo; si no puede hacerse, se ejecuta "except"
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
  print("Bienvenido.")
  print("MENÚ DE OPCIONES:")
  # Este ciclo imprime todas las opciones que tengo en la lista "options"
  for index, value in enumerate(options):
    print(f"{index + 1}. {value}.")
  print(f"#. Salir")
  selection = input("Elige la opción que desees ejecutar: ")
  # Validación del ingreso para seleccionar opciones del menú
  while True:
    try:
      # Con este if se hace la excepción del "#" necesario para salir del programa, ya que si no se tomaría como error debido a que no se puede convertir a entero
      if selection == "#":
        break
      selection = int(selection)
      # Esto funciona para que el usuario no ingrese una opción más de las que existen o menos de las que existen (que es 1)
      while selection > len(options) or selection < 1:
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
    # Separación de los datos por espacios
    preData = preData.split(" ")
    
    # Validación de datos
    dataNumber = 0
    for value in preData:
      data.append(validarDatos(value, dataNumber))
    dataNumber = len(data)

    # Cálculo de la media aritmética
    mediaAritmetica = sum(data)
    mediaAritmetica = mediaAritmetica / dataNumber
    
    # Cálculo de la desviación mediaAritmetica
    for value in data:
      desviacionMedia += abs(value - mediaAritmetica)
    desviacionMedia = desviacionMedia / dataNumber

    # Presentación de resultados
    print()
    print(f"Desviación media: {desviacionMedia}.")
    print(f"Media aritmética: {mediaAritmetica}.")
    print(f"Número de datos: {dataNumber}.")

    answer = ""
    answer = input(f"¿Deseas ver el procedimiento (s/n)? ").lower()
    if answer == "s":
      # Estos caracteres raros son para imprimir la raya encima de la x y así simular el símbolo de promedio
      print(f"_\nx = Σx / N")
      print(f"_\nx = (", end="")
      for index, value in enumerate(data):
        # Esta condición permite que el último dato no contenga el símbolo "+" después de su impresión; el argumento "end" es para que al terminar de imprimir imprima lo que está en él
        if index == len(data) - 1:
          print(f"{value}) ", end=f"/ {dataNumber}\n")
        else:
          print(f"{value} + ", end="")
      print(f"_\nx = {mediaAritmetica}")

      print(f"          _\nDM = |x - x| / N")
      print(f"DM = (", end="")
      for index, value in enumerate(data):
        if index == len(data) - 1:
          print(f"|{value} - {mediaAritmetica}|) ", end=f"/ {dataNumber}\n")
        else:
          print(f"|{value} - {mediaAritmetica}| + ", end="")
      print(f"DM = {desviacionMedia}")
    print()
else:
  print(f"\nGracias por usar mi programa :D, vuelve pronto.\nDesarrollado y escrito por Samuel Marroquín G.")
  input("Presiona Enter para salir.")