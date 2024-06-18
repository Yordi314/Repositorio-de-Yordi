nombre = input("Introduce tu nombre: ")
matricula = input("Introduce tu matricula: ")

asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

calificaciones = [] 

for asignatura in asignaturas:
  while True:
    try:
      calificacion = float(input(f"Introduce tu nota de {asignatura}: "))
      if calificacion >= 0:
        calificaciones.append(calificacion)
        break
      else:
        print("La calificación no puede ser negativa. Por favor, ingresa una calificación válida.")
    except ValueError:
      print("Ingresa un valor numérico válido.")

media = sum(calificaciones) / len(calificaciones) 

print(f"El promedio del estudiante {nombre} con la matricula {matricula} es {media}")

pregunta = input("¿Desea ingresar otro usuario? (si/no): ")

while pregunta == "si":
    nombre = input("Introduce tu nombre: ")
    matricula = input("Introduce tu matricula: ")
    asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

    calificaciones = [] 

    for asignatura in asignaturas:
      while True:
        try:
          calificacion = float(input(f"Introduce tu nota de {asignatura}: "))
          if calificacion >= 0:
            calificaciones.append(calificacion)
            break
          else:
            print("La calificación no puede ser negativa. Por favor, ingresa una calificación válida.")
        except ValueError:
          print("Ingresa un valor numérico válido.")

    media = round(sum(calificaciones) / len(calificaciones))

    print(f"El promedio del estudiante {nombre} con la matricula {matricula} es {media}")

    pregunta = input("¿Desea ingresar otro usuario? (si/no): ")

else:
  print("El programa ha finalizado")
