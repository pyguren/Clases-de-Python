"""
Las listas son un conjunto de datos y valores bajo un único nombre

"""

# Definir listas forma 1
cantantes = ["2pac", "jennifer lópez", "Dake"]

# Definir listas forma 2

peliculas = list(("Batman", "spiderman", "ironman"))

# Definir listas forma 2

year = list(range(2020, 2050))
variada = ["Esteban", 43, 4.4, True, "Sologuren"]

"""
print(cantantes)
print(peliculas)
print(year)
print(variada)
"""

# Indices

pelicula = "otra cosa"
peliculas[1] = "gran torino"
peliculas[2] = "el hobit"
print(peliculas)


print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:1])
print(peliculas[2:])


# Añadir elementos a las listas

cantantes.append("vico C")
print(cantantes)


# Recorrer y mostrar una lista
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("----------- Listado de peliculas------------")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} . {pelicula}")
"""


# Listas multidimensionales

print("-------------- Listado de contactos ----------------")

contactos = [

    [
        "Esteban",
        "estebansologuren@gmail.com"

    ],
    [
        "Pedro",
        "pedro@pedro.com"

    ],
    [
        "Alberto",
        "alberto@alberto.com"

    ]

]
"""

print(contactos[1])
print(contactos[0][1])

"""
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
