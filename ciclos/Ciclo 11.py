# 11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

numero = int(input("introduce un numero de dos digitos: "))

digito1 = numero // 10
digito2 = numero % 10

print("Números entre 1 y cada dígito del número:", numero)

print(f"Numeros entre 1 y {digito1}: ")
for i in range(1, digito1 + 1):
    print(i)

print(f"Numeros entre 1 y {digito2}: ")
for i in range(1, digito2 + 1):
    print(i)