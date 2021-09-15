# Mihir Chaturvedi
# Roll number: 2019061

import random


def get_random_number():
    return str(random.randint(1, 10 ** 1023))


def get_otp(seed):
    otp = ""
    for i in range(6):
        otp += seed[random.randint(0, len(seed) - 1)]
    return otp


def main(print_numbers=True):
    random_number = get_random_number()
    otp = get_otp(random_number)
    if print_numbers:
        print(random_number)
        print(otp)


if __name__ == "__main__":
    main()
