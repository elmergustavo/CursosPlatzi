def es_primo(numero):  # Se define la funcion es_primo que recibe un numero como parametro
    contador = 0  # Iniciamos una variable contador en 0
    # Hacemos un bucle que recorra un rango desde 1 hasta el numero + 1, (recordemos que no es inclusivo por esto #sumamos +1 para que tome el numero)
    for i in range(1, numero + 1):
        if i == 1 or i == numero:  # Aquí preguntamos si i es igual a 1 o al numero
            continue  # si alguna de las dos condiciones es verdadera nos saltamos la linea y repetimos el bucle
        if numero % i == 0:  # si el numero al dividirlo por i nos da como resto 0
            # Le sumamos al contador 1, esta linea es igual a tipear(contador = contador + 1)
            contador += 1
    # Cuando finalize de hacer todas las validaciones preguntamos,
    # Si el contador es igual a 0, es decir si el numero al dividirlo por todos los numero entre 1 y el mismo
    # si las divisiones dieron inexactas entonces nunca tuvimos un resto igual a 0 quiere decir que el contador
    # nunca aumento
    if contador == 0:
        return True  # Si es verdadero retornamos Verdadero
    else:
        return False  # Si es falso retornamos Falso


def run():
    numero = int(input('Escribe un Número: '))

    # Esto es equivalente a tipear si es_primo(numero) == True:
    if es_primo(numero):  # Si el resultado de la funcion es_primo es Verdadera decimos
        print('Es primo')  # Es primo
    else:  # Si no
        print('No es primo')  # No es primo


if __name__ == "__main__":
    run()
