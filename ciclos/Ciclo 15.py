# 15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

multiplos = []

for i in range(1,61):
    if i % 3 == 0:
        multiplos.append(i)

print("La suma de los primeros 20 numeros múltiplos de 3 es: " + str(sum(multiplos)))

