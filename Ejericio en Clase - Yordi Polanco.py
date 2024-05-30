vocales = ["A", "E", "I", "O", "U","a","e","i","o","u"]
nombre = input("Ingresa un nombre: ")
contador = 0
for letra in nombre:
  if letra in vocales:
    contador += 1

if contador >= 3:
  print("El nombre tiene tres vocales")
else:
  print("El nombre no tiene tres vocales")