flag = 0

def validarDatos(value, index, flag):
  while True:
    try:
      value = int(value)
      return value
    except ValueError:
      if flag == 1:
        value = input(f"ERROR: Opción no válida ({'Enter' if value == '' else value}); inténtalo de nuevo: ")
        for 
      elif flag == 2:
        value = input(f"\nERROR: Dato no soportado ({'Enter' if value == '' else value}), por favor reemplázalo; posición {index + 1} en los datos que ingresaste: ")

options = [
  "Desviación media para una serie de datos",
  "Desviación media para datos agrupados en una distribución de frecuencias simple"
]

print("\nBienvenido.")
print("\nMENÚ DE OPCIONES:")
for index, value in enumerate(options):
  print(f"{index + 1}. {value}.")
selection = input("Elige la opción que desees ejecutar: ")
selection = validarDatos(selection, 0, 1)

if selection == 1:
  mediaAritmetica = 0
  dm = 0
  data = []
  print(f"\nINSTRUCCIONES DE USO:\nIngresa todos los datos separados por UN espacio, para finalizar presiona Enter.")
  preData = input("Datos: ")
  preData = preData.split(" ")
  # Validación de datos
  for index, value in enumerate(preData):
    data.append(validarDatos(value, index, 2))
  
  # Cálculo de la media aritmética
  for index, value in enumerate(data):
    if value != "":
      mediaAritmetica += value
    else:
      break
  mediaAritmetica = mediaAritmetica / (index + 1)
  print(mediaAritmetica)
  
  # Cálculo de la desviación mediaAritmetica
  for index, value in enumerate(data):
    dm += abs(value - mediaAritmetica)