"""
Hacer un programa que pida la nota de 15 alumnos y sacar por pantalla
cuantos estan aprobados y reprobados

"""

contador = 0
aprobados = 0
reprobados = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al alumno {contador}?: "))

    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1

    contador += 1

print(f"alumnos aprobados: {aprobados} / alumnos reprobados: {reprobados}")
