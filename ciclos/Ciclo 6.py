# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.
import math

numero = int(input("introduce un numero de tres digitos: "))

digito1 = numero // 100
digito2 = (numero % 100) // 10
digito3 = numero % 10

print("Números entre 1 y cada dígito del número:", numero)

print(f"Numeros entre 1 y {digito1}: ")
for i in range(1, digito1 + 1):
    print(i)

print(f"Numeros entre 1 y {digito2}: ")
for i in range(1, digito2 + 1):
    print(i)

print(f"Numeros entre 1 y {digito3}: ")
for i in range(1, digito3 + 1):
    print(i)