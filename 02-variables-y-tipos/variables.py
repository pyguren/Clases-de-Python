"""
Una variable es un contenedor de informacion que en su interior guarda informacion.
Se puede crear muchas variables y que cada una tenga informacion distinta
"""

# Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "Con Victor Robles"
numero = 88
decimal = 9.8

print("---------------------")

# Mostrar en la consola la informacion al interior de las variables

print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------")

# Cambiarle el valor a las variables y mostrarla en consola
numero = 99
decimal = 8.6
print(numero)
print(decimal)

print("---------------------")

# Concatenación

nombre = ("Esteban")
apellido = ("Sologuren")
web = ("proyectistadegas.cl")

# concatenacion simple
print(nombre + " " + apellido + " " + web)

#concatenacion usando corchetes
print(f"{nombre} {apellido} {web}")

#concatenacion usando el metodo format
print("Hola me llamo {} {} y mi sitio web es {}".format(nombre, apellido, web))