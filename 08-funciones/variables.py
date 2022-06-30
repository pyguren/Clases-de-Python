"""
Variables locales: Se definen dentro de una funcion y no pueden ser utilizadas fuera de ellas

Variables globales: Se declaran fuera de las funciones y pueden ser utilizadas dentro y fuera de ellas

"""

# Variable global
from asyncio.base_subprocess import WriteSubprocessPipeProto


frase = "Hola a todos!!!"

print(frase)


def holaMundo():
    # Variable local
    frase = "Hola mundo.."

    # Hay una forma de convertir una variable local en variable global y es anteponiendo el
    # término "global" al nombre de la variable

    global website
    website = "tecnicodecalefon.cl"

    print(frase)
    print("Desde dentro de la funcion ", website)


print(holaMundo())
print("Fuera de la funcion", website)
