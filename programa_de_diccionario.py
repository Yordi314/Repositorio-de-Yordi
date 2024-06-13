divisas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥', 'Peso mexicano':'MXN$', 'Real':'R$'}

divisa = input("Introduce una divisa: ")

if divisa in divisas:
  print(f"El símbolo de {divisa} es {divisas[divisa]}")
else:
  print(f"La divisa {divisa} no está en el diccionario.")
