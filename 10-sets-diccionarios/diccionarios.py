"""
Es un tipo de dato que almacena un conjunto de datos en formato clave > valor.
Es parecido a lo que en otros lenguajes se llama un array asociativo o un objeto json

"""
"""

personas = {

    "nombre": "Esteban",
    "apellidos": "Sologuren",
    "web": "tecnicodecalefon.cl"

}

print(personas)
"""

# Listas con diccionarios


contactos = [
    {
        "nombre": "Esteban",
        "mail": "esteban@esteban.com"

    },
    {
        "nombre": "luis",
        "mail": "luis@luis.com"

    },
    {
        "nombre": "pepe",
        "mail": "pepe@pepe.com"

    }


]

print(contactos[0]["nombre"])

print("\nListado de contactos: ")
print("---------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['mail']}")

    print("---------------------------")
