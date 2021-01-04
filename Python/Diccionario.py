Diccionario = { #Los diccionarios pueden guardar datos de diferentes formatos, es decir, tanto string como numérico
    "Alumno":"Pedro Gutierres", #Los elementos que se encuentra a la izquierda de los dos puntos se los denominan "llaves", mientras que los valores que estan a la derecha se los denomina "valor"
    "Edad" :23,
    "Carrera": "Geología",
    "Promedio":7.89,
}

print(Diccionario["Alumno"]) #Permite mostrar el valor que se encuentra dentro de la llave "Alumno"

print(f'El estudiante {Diccionario["Alumno"]} de {Diccionario["Edad"]} años de edad se encuentra estudiando {Diccionario["Carrera"]} y lleva un promedio de {Diccionario["Promedio"]}')

#PARA REEMPLAZAR UN VALOR EXISTENTE

Diccionario['Carrera'] = 'Biologia' #Reemplaza el valor que se encuentra dentro de la llave Geologia
print(Diccionario)

#PARA ELIMINAR UN VALOR EXISTENTE

del Diccionario['Promedio'] #Elimina el promedio
print(Diccionario)