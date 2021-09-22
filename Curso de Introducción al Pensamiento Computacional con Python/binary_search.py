# objetivo = int(input('Escoge un entero: '))
# epsilon = 0.00001
# bajo = 0.0
# alto = max(1.0, objetivo)
# respuesta = (alto + bajo) / 2

# while abs(respuesta**2 - objetivo) >= epsilon:
#     if respuesta**2 < objetivo:
#         bajo = respuesta
#     else:
#         alto = respuesta

#     respuesta = (alto + bajo) / 2

# print(f'La raiz cuadrada del {objetivo} es la {respuesta}')


def binary_search():
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.00001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada del {objetivo} es la {respuesta}')

if __name__ == "__main__":
    binary_search()
