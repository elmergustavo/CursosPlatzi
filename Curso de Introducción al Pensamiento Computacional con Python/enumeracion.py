# 'saber si un numero tiene una raiz exacta'

# objetivo = int(input('Escoge un entero: '))
# respuesta = 0
 
# while respuesta**2 < objetivo:
#     print(respuesta)
#     respuesta += 1

# if respuesta**2 == objetivo:
#     print(f'La raiz cuadrada de  {objetivo} es {respuesta}')
# else:
#     print(f'{objetivo} no tiene una raiz cuadrada exacta')


def enumeracion_exahustiva():
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        # print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada {objetivo} es {respuesta}')


if __name__ == "__main__":
    enumeracion_exahustiva()

