# 5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

numero_uno = int(input("Introduce un primer numero: "))
numero_dos = int(input("Introduce un segundo numero: "))

for i in range(numero_uno, numero_dos + 1):
    if i % 10 == 4:
        print(i)
