# 1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.

numero = int(input("Introduce un numero mayor que 1: "))

print(f"Numeros entre 1 y {numero}:")

for i in range(1, numero + 1):
    print(i)