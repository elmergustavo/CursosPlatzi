# objetivo = int(input('Escoge un entero: '))
# epsilon = 0.01
# paso = epsilon**2
# respuesta = 0.0

# while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
#     # print(abs(respuesta**2 - objetivo), respuesta)
#     respuesta += paso

# if abs(respuesta**2 - objetivo) >= epsilon:
#     print(f'No se encontro la raiz cuadrada {objetivo}')
# else:
#     print(f'La raiz cuadrada {objetivo} es {respuesta}')

def numeric_aproximation():
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
    numeric_aproximation()

