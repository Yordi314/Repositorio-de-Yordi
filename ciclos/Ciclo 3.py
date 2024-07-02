# 3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

numero = int(input("Introduce un numero mayor a 1: "))

print(f"Divisores exactos del {numero} entre 1 y dicho numero: ")

for i in range(1, numero + 1):
  if numero % i == 0:
    print(i)