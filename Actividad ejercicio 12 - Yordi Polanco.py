numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el segundo número entero: "))

numero_par = [0, 2, 4, 6, 8]
numero_primo = [2, 3, 5, 7]

diferencia = numero_uno - numero_dos

digito_uno = int((diferencia / 10))
digito_dos = round((diferencia % 10))

digitos_sum = digito_uno + digito_dos

contador = 0
contador_dos = 0

for n in numero_par:
  if digito_dos == int(n):
    contador =+ 1

if contador == 1:
  print(f"El numero {diferencia} es par y la suma de sus digitos es: {digitos_sum}",)
else:
  print(f"El numero {diferencia} es impar")

for n in numero_primo:
  if diferencia == int(n):
    contador_dos =+ 1

if contador_dos == 1:
  print("La diferencia es un número primo y el producto es:", numero_uno * numero_dos)
elif contador_dos == 0:
  print("La diferencia no es un número primo")

if str(diferencia).endswith('4'):
  digito_uno_entero_uno = int(numero_uno / 10)
  digito_dos_entero_uno = round(numero_uno % 10)
  digito_uno_entero_dos = int(numero_dos / 10)
  digito_dos_entero_dos = round(numero_dos % 10)
  print(f"El numero {diferencia} termina en 4 y los digitos por separado son: ")
  print(f"{digito_uno_entero_uno}, {digito_dos_entero_uno}, {digito_uno_entero_dos}, {digito_dos_entero_dos}")