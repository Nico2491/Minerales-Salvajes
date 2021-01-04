
"""

#CASO 1
programas = ['Python', 'JavaScript', 'Java', 'C++'] 

if 'Java' in programas:
    print('Descuento 20%')
else:
    print('No hay descuento')



#DOS MANERAS DIFERENTES DE HACER LO MISMO

#CASO 2

likes = 10
encanta = 100

if likes == 200:
    if encanta == 300:
        print('Llegaste a 200 likes y 300 encanta') #Si se cumple las la primer y segunda condición, entonces se muestra este mensaje
    else:
        print('Llegaste solo a 200 likes pero faltan encanta') #Si se cumple las la primer y pero no la segunda condición, entonces se muestra este mensaje
else:
    if encanta == 300:
        print('Llegaste a los 300 encanta pero faltan likes') #Si no se cumple las la primer y pero si la segunda condición, entonces se muestra este mensaje
    else:
        print('Faltan likes y encanta') #Si no se cumple ninguna de las dos condiciones, entonces se muestra este mensaje
"""
#CASO 3
"""
likes = 100
encanta = 100

if likes == 200 and encanta == 300:
    print('Llegaste a 200 likes y 300 encanta')
elif likes == 200 and encanta < 300:
    print('Llegaste solo a 200 likes pero faltan encanta')
elif likes < 200 and encanta == 300:
    print('Llegaste a los 300 encanta pero faltan likes')
else:
    print('Faltan likes y encanta')

#CASO 4 - OTRO EJEMPLO
"""
"""
Saldo_Banco_Nacion = 700
Mercado_Pago = 700
Juguete = 500
"""
#CASO 5 con funcion

def compra(Juguete, MercadoPago, SaldoBancoNacion):
    if Juguete <= MercadoPago and Juguete <= SaldoBancoNacion:
        print("Puedes comprar el juguete por alguno de los dos medios")
    elif Juguete >= MercadoPago and Juguete <= SaldoBancoNacion:
        print("Puedes comprarlo con la tarjeta del banco nación")
    elif Juguete <= MercadoPago and Juguete >= SaldoBancoNacion:
        print("Puedes comprarlo con Mercado Pago")
    else:
        print("Estas fundido amigo")   


compra(1000, 1200, 700) 

