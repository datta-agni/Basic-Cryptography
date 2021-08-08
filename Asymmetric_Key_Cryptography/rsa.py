# basic implementation of Rivest–Shamir–Adleman algorithm
import random

# change the max_PrimeLength for longer keys and security
n = int(input("Enter the key size: "))
max_PrimLength = 10 ** n
low_PrimLength = 10 ** (n - 1)

# calculates the modular inverse from e and phi
def euler_totient(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euler_totient(b % a, a)
        return (g, x - (b // a) * y, y)


# calculates the gcd of two integers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# check composite number for rabin-miller primality tes
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    # n  is definitely composite
    return True


# checks if a number is a prime through miller-rabin primality test
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(
        _try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n]
    )


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def generateRandomPrim():
    while 1:
        ranPrime = random.randint(low_PrimLength, max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime


def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()

    n = p * q
    print("n ", n)
    # phi(n) = phi(p)*phi(q)
    phi = (p - 1) * (q - 1)
    print("phi ", phi)

    # choose e coprime to n and 1 > e > phi
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    print("e=", e, " ", "phi=", phi)
    # d[1] = modular inverse of e and phi
    d = euler_totient(e, phi)[1]

    # make sure d is positive
    d = d % phi
    if d < 0:
        d += phi

    return ((e, n), (d, n))


def decrypt(ciphertext, private_key):
    try:
        key, n = private_key
        text = [chr(pow(char, key, n)) for char in ciphertext]
        return "".join(text)
    except TypeError as e:
        print(e)


def encrypt(text, public_key):
    key, n = public_key
    ciphertext = [pow(ord(char), key, n) for char in text]
    return ciphertext


def main():
    public_key, private_key = generate_keyPairs()
    text = str(input("Enter the text you want to be encrypted with RSA: "))

    print("Public: ", public_key)
    print("Private: ", private_key)

    ciphertext = encrypt(text, public_key)
    print("encrypted  =", ciphertext)
    plaintext = decrypt(ciphertext, private_key)
    print("decrypted =", plaintext)


if __name__ == "__main__":
    main()
