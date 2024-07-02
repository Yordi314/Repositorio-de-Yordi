# 16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

numero_uno = int(input("Introduce un primer numero: "))

numero_dos = int(input("Introduce un segundo numero: "))

multiplos_de_dos = []

for i in range(1, numero_uno + 1):
    if i % 2 == 0:
        multiplos_de_dos.append(i)

promedio_dos = sum(multiplos_de_dos) / numero_uno

multiplos_de_cinco = []

for i in range(1, numero_dos + 1):
    if i % 2 == 0:
        multiplos_de_cinco.append(i)

promedio_cinco = sum(multiplos_de_cinco) / numero_uno

if promedio_dos > promedio_cinco:
  print(f"El promedio de los {numero_uno} primeros múltiplos de 2 es mayor que el promedio de los {numero_dos} primeros múltiplos de 5.")
else:
  print(f"El promedio de los {numero_uno} primeros múltiplos de 2 no es mayor que el promedio de los {numero_dos} primeros múltiplos de 5.")