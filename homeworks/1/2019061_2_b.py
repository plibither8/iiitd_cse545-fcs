# Mihir Chaturvedi
# Roll number: 2019061

from gmpy2 import mpz_random, random_state
import time
import random


def get_random_number():
    random_number = (10 ** 1022) + mpz_random(
        random_state(time.time_ns()), (10 ** 1023) - (10 ** 1022) - 1
    )
    return str(random_number)


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
    return otp


if __name__ == "__main__":
    main()
