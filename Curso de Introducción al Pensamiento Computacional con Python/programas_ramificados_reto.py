user_1 = input('Ingresa el nombre del primer usuario: ')
age_1 = int(input('Escoge un edad: '))

user_2 = input('Ingresa el nombre del segundo usuario: ')
age_2 = int(input('Escoge su edad: '))

if age_1 > age_2:
    print(F'El usuario {user_1} es mayor que el usuario {user_2}')
elif age_1 < age_2:
    print(F'El usuario {user_1} es menor que el usuario {user_2}')
else:
    print(f'{user_1} y {user_2} tienen la misma edad')
