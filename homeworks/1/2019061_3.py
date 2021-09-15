# Mihir Chaturvedi
# Roll number: 2019061

import gmpy2
import random


def alice_sends_bob(p, g):
    a = gmpy2.mpz_random(gmpy2.random_state(random.randint(0, 1023)), 10 ** 1023)
    A = gmpy2.powmod(g, a, p)
    print("a = ", a)
    print("A = ", A)
    return (A, a)


def bob_sends_alice(p, g):
    b = gmpy2.mpz_random(gmpy2.random_state(random.randint(0, 1023)), 10 ** 1023)
    B = gmpy2.powmod(g, b, p)
    print("b = ", b)
    print("B = ", B)
    return (B, b)


def print_shared_secret_alice(B, a, g):
    S = gmpy2.powmod(B, a, g)
    print("S = ", S)
    return S


def print_shared_secret_bob(A, b, g):
    S = gmpy2.powmod(A, b, g)
    print("S = ", S)
    return S
