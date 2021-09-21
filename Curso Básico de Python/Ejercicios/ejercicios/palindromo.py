def palindromo(palabra):  # Definimos una función que recibira como parametro la palabra
    # A la palabra le eliminamos los espacios y la convertimos en minuscula
    palabra = palabra.replace(' ', '').lower()
    # Generamos la palabra invertida apartir de la palabra original
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:  # Preguntamos si la palabra es igual a la palabra invertida
        return True  # Si sí devolvemos verdadero
    else:  # Si no
        return False  # Devolvemos fals


def run():  # Funcion principal
    # Solicitamos una palabra y la guardamos en una variable
    palabra = input('Escribe una palabra: ')
    # ejecutamos la funcion palindromo y le pasamos como parametro la variable con la palabra solicitada
    # Guardamos lo que retorne esta funcion en una variable
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:  # Preguntamos si lo que retorna la funcion es verdadero
        print('Es palindromo')  # Sì si, decimos que es palindromo
    else:  # Si no
        print('No es palindromo')  # No es palindromo


if __name__ == "__main__":
    run()
