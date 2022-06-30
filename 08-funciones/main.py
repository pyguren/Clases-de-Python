"""
Funciones:

Una función es un conjunto de instrucciones agrupadas en un nombre en concreto
que pueden reutilizarse invocando a la funcion tantas veces sea necesario.


def nombreDeLaFuncion(parametros):
    #bloques / conjunto de instrucciones

"""
# Definir funciones e invocarlas


"""
print("########## Ejemplo 1 ###########")


def muestraNombre():
    print("Carlos")
    print("Juan")
    print("José")
    print("Mario")


muestraNombre()

# Parámetros

"""
"""
print("########## Ejemplo 2 ###########")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad > 18:
        print("Y eres mayor de edad")
    else:
        print("Y eres menor de edad")


nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cual es tu edad? "))
mostrarTuNombre(nombre, edad)

"""
"""
print("########## Ejemplo 3 ###########")


def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(1, 11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")


tabla(8)

print("--------------------------------------------")
# Ejemplo 3.1

for numero_tabla in range(1, 11):
    tabla(numero_tabla)

"""
print("--------------------------------------------")

"""
print("########## Ejemplo 4 ###########")
# Parámetros opcionales


def getEmpleados(nombre, dni=None):
    print("Empleados")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")


getEmpleados("Esteban Sologuren", "15.320.317-2")

"""
# Ejemplo 5 - Return y devolver datos
"""
print("\n########## Ejemplo 5 ###########")


def saludame(nombre):
    saludo = f"Hola {nombre} ¿Como estás?"

    return saludo


print(saludame("Esteban Sologuren"))

"""
# Ejemplo 6 - Calculadora
print("\n########## Ejemplo 6 ###########")


def calculadora(numero1, numero2, basicas=False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return(cadena)


print(calculadora(29, 88, True))


# Ejemplo 7 - Usar una función dentro de otra funcion
print("\n########## Ejemplo 7 ###########")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo("Esteban", "Sologuren Jamette"))


# Ejemplo 8 - Funciones lambda
print("\n########## Ejemplo 8 ###########")


def dime_el_year(year): return return f"El año es {year}"


print(dime_el_year(2022))
