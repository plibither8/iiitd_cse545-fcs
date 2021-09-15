# Mihir Chaturvedi
# Roll number: 2019061

import gmpy2
import random


def encrypt(m, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gmpy2.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    c = gmpy2.powmod(m, e, n)
    d = gmpy2.invert(e, phi)

    print("c = ", c)
    print("e = ", e)
    print("d = ", d)
    print("n = ", n)

    return (c, d, n)


def decrypt(c, d, n):
    m = gmpy2.powmod(c, d, n)
    print("m = ", m)
    return m


# decrypt(*encrypt(123123, 39461, 44293))
