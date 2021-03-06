# Mihir Chaturvedi
# Roll number: 2019061

import time

import gmpy2


def bob_sends_alice(p, g):
    b = gmpy2.mpz_random(gmpy2.random_state(time.time_ns()), 10 ** 1023)
    B = gmpy2.powmod(g, b, p)
    # print("b =", b)
    # print("B =", B)
    return (B, b)


def alice_sends_bob(p, g):
    a = gmpy2.mpz_random(gmpy2.random_state(time.time_ns()), 10 ** 1023)
    A = gmpy2.powmod(g, a, p)
    # print("a =", a)
    # print("A =", A)
    return (A, a)


def print_shared_secret_alice(B, a, p):
    S = gmpy2.powmod(B, a, p)
    print("S =", S)
    return S


def print_shared_secret_bob(A, b, p):
    S = gmpy2.powmod(A, b, p)
    print("S =", S)
    return S


if __name__ == "__main__":
    p = gmpy2.mpz(input("p = "))
    g = gmpy2.mpz(input("g = "))

    (B, b) = bob_sends_alice(p, g)
    (A, a) = alice_sends_bob(p, g)

    print_shared_secret_alice(B, a, p)
    print_shared_secret_bob(A, b, p)
