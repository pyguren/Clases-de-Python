nombre = "esteban"

# Funciones generales

print(type(nombre))

# Detectar el tipado

comprobar = isinstance(nombre, str)

if comprobar:
    print("Esta variable es un string")
else:
    print("Esta variable NO es un string")

if not isinstance(nombre, float):
    print("Esta variable NO es un numero con decimales")

# Limpiar espacios

frase = "     mi contenido           "
print(frase)
print(frase.strip())

# Eliminar variables

year = 2022
print(year)
del year
# print(year)

# Saber cuantos caracteres tiene una variable

texto = "fffggg"

if len(texto) <= 0:
    print("Esta variable esta vacia")
else:
    print("Esta variable tiene: ", len(texto),  "caracteres")

# Encontrar caracteres

frase = "la vida es bella"

print(frase.find("vida"))

# Reemplazar palabras en un string

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())
