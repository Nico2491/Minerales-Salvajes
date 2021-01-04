#LISTS (ARREGLOS)
#Para crear "Lists" se tienen que usar corchetes

#RECORDAR QUE LOS ARRAYS EN PYTHON ARRANCAN DESDE EL VALOR CERO Y NO DESDE EL VALOR 1!!

#CASO 1
lenguaje = ['Python', 'JavaScript', 'Java', 'C++'] 

print(lenguaje)
print(lenguaje[3]) #Selecciona el valor que se encuentra en la posición (C++)

#CASO 2

lenguaje.sort() #Permite ordenar los de la lista alfabeticamente
print(lenguaje)
print(lenguaje[3]) #En este caso, el que se encuentra en la última posición es python ya que fueron ordenados alfabeticamente

#CASO 3

lenguaje.reverse() #Ordena los elementos de manera al reves de como estaban inicialmente
print(lenguaje)

#CASO 4

Aprendiendo = f'Estoy aprendiendo {lenguaje[3]}' #La letra "f" se utiliza cuando quiero mezclar variables con strings
print(Aprendiendo)

#CASO 5

lenguaje[2] = 'PHP' #reemplaza el valor que se encuentra en la posición 2 (en este caso Javascript) por PHP
print(lenguaje) 

#CASO 6

lenguaje.append ('Matlab') #"append" Permite agregar un nuevo lenguaje a la lista inicial que teniamos de lenguajes
print(lenguaje)

#CASO 7
lenguaje.pop(0) #Borra el lenguaje que se encuentra en la posición 0 (C++)
print(lenguaje)

#CASO 8
lenguaje.pop() #Si no indico la posición, automaticamente elimina el último elemento de la lista
print(lenguaje)

#CASO 9

lenguaje.remove('C++') #Se indica el nombre del elemento de la lista que queremos eliminar
print(lenguaje)