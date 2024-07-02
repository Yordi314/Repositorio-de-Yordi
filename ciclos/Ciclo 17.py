suma_numeros_5 = 0
cantidad_numeros_5 = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
  if numero % 10 == 5:
    suma_numeros_5 += numero
    cantidad_numeros_5 += 1
  numero = int(input("Ingrese un número (0 para terminar): "))

if cantidad_numeros_5 > 0:
  promedio = suma_numeros_5 / cantidad_numeros_5
  print("El promedio de los números terminados en 5 es:", promedio)
else:
  print("No se ingresaron números terminados en 5.")