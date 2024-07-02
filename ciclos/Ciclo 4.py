# 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

numero_uno = int(input("Introduce un primer numero: "))
numero_dos = int(input("Introduce un segundo numero: "))

print(f"Numeros comprendidos entre {numero_uno} y {numero_dos}: ")

for i in range(numero_uno, numero_dos + 1):
    print(i)
