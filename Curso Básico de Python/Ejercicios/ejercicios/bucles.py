def run():
    LIMITE = 100000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) +
              ' es igual a: ' + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()
