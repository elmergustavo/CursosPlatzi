import random
import string


def generator_password():
    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    simbols = list(string.punctuation)
    numbers = list(string.digits)

    characteres = mayus + minus + simbols + numbers
    password = []

    for i in range(15):
        character_random = random.choice(characteres)
        password.append(character_random)

    password = ''.join(password)
    return password


def run():
    password = generator_password()
    print('Your new password is: ' + password)


if __name__ == "__main__":
    run()
