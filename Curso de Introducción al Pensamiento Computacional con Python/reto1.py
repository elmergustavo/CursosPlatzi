def enumeracion_exahustiva(objetivo):
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

def numeric_aproximation(objetivo):
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

def binary_search(objetivo):
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

def main():
    objetivo = int(input('Escoge un entero: '))
    method = int(input(
        f'Escoge un metodo: \n'
        f'[0] enumeracion exhahustiva\n'
        f'[1] Aproximacion\n'
        f'[2] Busqueda Binaria\n'
    ))

    action = {
        0: enumeracion_exahustiva,
        1: numeric_aproximation,
        2: binary_search,
    }

    action[method](objetivo)

if __name__ == "__main__":
    main()
