def run():
    mi_diccionario = {
        # Los elementos tienen que ir separados por coma
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 4493872,
        'Brazil': 1023102312,
        'Colombia': 50372424,
    }

    # print(poblacion_paises['Argentina'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    # print(pais)

    # Como el metodo nos devuelve dos elementos tenemos que agregar un segundo
    # elemento iterador en el for para no tener errores
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == "__main__":
    run()
