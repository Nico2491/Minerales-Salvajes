
#A partir de la funcion "return", retorna los datos guardados que fueron ingresados por el usuario en una variable llamada "Información_cliente" que posteriormente es mostrada a partir del comando "print"

#DOS MANERAS DE HACER LO MISMO 

#MANERA 1

"""
def informacion(nombre = "n/a", edad = "n/a", DeporteFavorito = "n/a"): #Se establecieron valores por default predeterminado en caso que le usuario no ingrese la información solicitada
    return nombre, edad, DeporteFavorito

Informacion_cliente = informacion('Alfonso', '25')

print(Informacion_cliente)"""

#MANERA 2

#En este caso, ingreso los valores dentro de variables y luego las utilizo en la funcion

NombreCompleto='Juan Gonzales'
años = 25

def informacion(nombre = "n/a", edad = "n/a", DeporteFavorito = "n/a"): #Se establecieron valores por default predeterminado en caso que le usuario no ingrese la información solicitada
    return nombre, edad, DeporteFavorito

Informacion_cliente = informacion(NombreCompleto, años) #Información del usuario guardada dentro de la variable "Informacion_cliente"

print(Informacion_cliente)