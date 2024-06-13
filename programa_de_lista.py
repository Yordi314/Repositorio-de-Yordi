asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua", "Ingles"]
asignaturas_quemadas = []

for asignatura in asignaturas:
  calificacion = float(input(f"Introduce tu nota de {asignatura}: "))
  if calificacion < 70:
    asignaturas_quemadas.append(asignatura)

print("Tienes que repetir las siguientes asignaturas:")

for asignatura in asignaturas_quemadas :
  print(asignatura)
