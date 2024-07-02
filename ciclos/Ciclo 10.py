# 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.

numero = int(input("Introduce un numero mayor que 1: "))

print(f"Suma de los todos los numeros comprendidos entre 1 y {numero}:")

suma = []

for i in range(1, numero + 1):
    suma.append(i)

print(sum(suma))