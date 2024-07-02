# 12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

numero = int(input("Introduce un numero de tres digitos: "))

digito1 = numero // 100
digito2 = (numero % 100) // 10
digito3 = numero % 10

digitos = [digito1, digito2, digito3]

contador = 0

for i in digitos:
    if i == 1:
        contador += 1
    else:
        contador = 0

if contador >= 1:
    print(f"El numero {numero} tiene un digito 1")
else:
    print(f"El numero {numero} no tiene un digito 1")