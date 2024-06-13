numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

numero_random = int(input("Introduce un número random entre 1 y 20: "))

for n in numeros:
  if numero_random == n:
    print(f"El número {numero_random} está en la tupla")
    break

else:
  print(f"El número {numero_random} no está en la tupla")
