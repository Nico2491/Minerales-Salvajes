lista = ['Python', 'JavaScript', 'Java', 'C++'] 

for lenguaje in lista: #Este ciclo for recorre toda la lista poniendo en minuscula aquellos lenguajes que no son "Java" y pone en mayuscula el lenguaje "Java"
    if lenguaje == 'Java':
        print(lenguaje.upper())
    else:
        print(lenguaje.casefold())