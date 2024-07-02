# 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.

numero = int(input("Ingrese un número entero: "))

suma_factoriales = 0
for i in range(1, numero + 1):
  factorial = 1
  for j in range(1, i + 1):
    factorial *= j
  suma_factoriales += factorial

print(f"La sumatoria de las factoriales de los números entre 1 y {numero} es: {suma_factoriales}")