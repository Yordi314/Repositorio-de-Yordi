# 2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

numero = int(input("Introduce un numero mayor a 1: "))

print(f"Numeros pares entre 1 y {numero}:")

for i in range(2, numero + 1, 2):
    print(i)