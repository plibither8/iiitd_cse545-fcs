# Mihir Chaturvedi
# Roll number: 2019061

import random


def get_random_number():
    start = 10 ** 2022
    end = (10 ** 2023) - 1
    return str(random.randint(start, end))


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
