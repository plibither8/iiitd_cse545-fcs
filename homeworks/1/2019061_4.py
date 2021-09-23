# Mihir Chaturvedi
# Roll number: 2019061

import gmpy2
import sys


def encrypt(m, p, q):
    if p == q:
        print("p and q should be different")
        exit(1)

    if p > q:
        print("p should be smaller than q")
        exit(1)

    if not gmpy2.is_prime(p) or not gmpy2.is_prime(q):
        print("p and q should be prime")
        exit(1)

    n = gmpy2.mul(p, q)
    phi = gmpy2.mul(p - 1, q - 1)
    e = gmpy2.next_prime(q)
    c = gmpy2.powmod(m, e, n)
    d = gmpy2.invert(e, phi)

    print("c =", c)
    print("e =", e)
    print("d =", d)
    print("n =", n)

    return (c, d, n)


def decrypt(c, d, n):
    m = gmpy2.powmod(c, d, n)
    print("m =", m)
    return m


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Specify 'encrypt' or 'decrypt'")
        exit(1)

    if sys.argv[1] == "encrypt":
        m = gmpy2.mpz(input("m = "))
        p = gmpy2.mpz(input("p = "))
        q = gmpy2.mpz(input("q = "))
        print()

        encrypt(m, p, q)
        exit()

    if sys.argv[1] == "decrypt":
        c = gmpy2.mpz(input("c = "))
        d = gmpy2.mpz(input("d = "))
        n = gmpy2.mpz(input("n = "))
        print()

        decrypt(c, d, n)
        exit()

    print("Specify 'encrypt' or 'decrypt'")
