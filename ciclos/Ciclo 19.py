# 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.

numero = int(input("Ingrese un número entero: "))

for i in range(1, 11):
  producto = numero * i
  print(numero, "x", i, "=", producto)