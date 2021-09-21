def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuántos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos 🇴
2 - Pesos Argentinos 🇷
3 - Pesos mexicanos 🇽

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875)

elif opcion == 2:
    conversor('Argentinos', 65)
elif opcion == 3:
    conversor('Mexicanos', 24)
else:
    print('Ingrese una opción Correcta por favor')


###    DOLARES A PESOS COLOMBIANOS ###

# Solicitamos el valor en dolares y lo convertimos a flotante
# dolar = float(input('¿Cúantos dólares tienes?: '))

# # hacemos la operacion multiplicando el valor del dolar en peso colombiano por cada dolar que poseé el usuario
# # lo redondeamos y lo convertimos a string a la vez
# peso_cop = str(round(valor_dolar * dolar, 1))

# print('Tienes $'+peso_cop+' Pesos Colombianos')
