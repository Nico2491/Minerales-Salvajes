#CREAR FUNCION QUE IMPRIMA UN MENSAJE DE BIENVENIDA
"""
def hola():
    print('Bienvenido a casa!') #En este caso no lleva la letra "f" porque no hay una variable 

hola()

"""

#CREAR FUNCION QUE TOME EL NOMBRE DE UN USUARIO E IMPRIMA UN MENSAJE DE BIENVENIDA 

#MANERA 1

"""
def Saludo(nombre):
    print(f'Bievenido {nombre}, como estas?')

Saludo('Juan')

"""


#MANERA 2

Persona = 'Juan Torres'

def Saludo(Nombre):
    print(f'Bievenido {Nombre}, como estas?')

Saludo(Persona) #En este caso estoy ingresando una variable dentro de la función
