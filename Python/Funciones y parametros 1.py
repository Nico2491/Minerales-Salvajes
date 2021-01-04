
#COMANDOS PARA CREAR FUNCIONES

"""Los comentarios se pueden hacer con hashtag (si es solo una línia) o con doble comilla si son varias lineas"""

"""La Función es "informacion" y "nombre y horario" son parametros"""

#UNA MANERA

"""

def informacion(nombre):
    print(f'Bienvenido a casa {nombre}') #Cuando ejecuto una variable, tengo que poner una "f" al principio para que me lea bien el comando

informacion('Juan') 
informacion('Ramiro')
informacion('Rodolfo')

"""
#OTRA MANERA

def informacion(nombre, puesto, horario = 'n/a'): #Al igualar un parámetro, permite establecer por default un valor determinado en caso que el usuario no haya ingresado información solicitada
    print(f'Bienvenido a casa {nombre} y soy {puesto}. Registrado a las {horario}') #Cuando ejecuto una variable dentro de la oracion escrita, tengo que poner una "f" al principio para que me lea bien el comando

#El usuario ingresa los parametros establecidos y luego se ejecuta la funcion
informacion('Juan', 'Programador', '11:30') 
informacion('Ramiro', 'Geólogo', '21:15')
informacion('Rodolfo', 'Panadero')


