
"""
# condicional IF

if condicion:
    instrucciones
    
else:
    otras instrucciones


# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos

and  Y
or  O
!  negacion
not  NO


"""

# ejercisio 1

print("############ejercisio 1################")

color = "rojo"
# color = input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("Enhorabuena!!!")
    print("El color es rojo")
else:
    print("Color incorrecto")

# ejersicio 2

print("\n############ejersicio 2################")

year = 2020

# year = int(input("¿En que año estamos?"))

if year >= 2021:
    print("Estamos en un año mayor a 2020")
else:
    print("Es un año menor a 2021")
    
# ejersicio 3

print("\n############ejersicio 3################")

nombre = "Esteban"
edad = 43
ciudad = "Concón"
continente = "america"
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "america":
        print("No eres americano")
    else:
        print(f"{nombre} es americano y de la ciudad de {ciudad}")
    
else:
    print(f"{nombre} no es mayor de edad")
    
# ejersicio 4

print("\n############ejersicio 4################")

# dia = int(input("¿Que numero de dia de la semana es hoy?: "))
dia = 1
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")
    
# ejersicio 5

print("\n############ ejersicio 5 ################")

edad_minima = 18
edad_maxima = 65
# edad_oficial = int(input("¿Tienes edad para trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Tienes edad suficiente para trabajar")
else:
    print("No tienes edad suficiente para trabajar")
    
# ejersicio 6

print("\n############ ejersicio 6 ################")

pais = "alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia" :
    print(f"{pais} es un pais de habla hispana") 
else:
    print(f"{pais} No es un pais de habla hispana")
    
# ejersicio 7

print("\n############ ejersicio 7 ################")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia") :
    print(f"{pais} NO es un pais de habla hispana") 
else:
    print(f"{pais} SI es un pais de habla hispana")
    
# ejersicio 8

print("\n############ ejersicio 8 ################")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia" :
    print(f"{pais} NO es un pais de habla hispana") 
else:
    print(f"{pais} SI es un pais de habla hispana")