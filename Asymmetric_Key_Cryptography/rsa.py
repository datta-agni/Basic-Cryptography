# basic implementation of Rivest–Shamir–Adleman algorithm
"""
Used for generating random numbers used for prime checking
"""
import random

"""
Returns a non-negative Python integer with k random bits. This method is supplied with the MersenneTwister Generator
"""
maximum_prime_length = int(input("Enter the number of bits for generation: "))


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


# check composite number for rabin-miller primality test
def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    # n  is definitely composite
    return True


# checks if a number is a prime through miller-rabin primality test
def is_prime(n, precision_for_huge_n=16):
    if n in known_primes:
        return True
    if any((n % p) == 0 for p in known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(
        try_composite(a, d, n, s) for a in known_primes[:precision_for_huge_n]
    )


known_primes = [2, 3]
known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

# function used to generate random number which inturn are checked for being prime
def generate_random_prime():
    while 1:
        ranPrime = random.getrandbits(maximum_prime_length)
        if is_prime(ranPrime):
            return ranPrime


# function used to generate the public-key, private-key pair
def generate_key_pair():
    p = generate_random_prime()
    q = generate_random_prime()

    n = p * q
    print("n:\n", n)
    # phi(n) = phi(p)*phi(q)
    phi = (p - 1) * (q - 1)
    print("phi:\n", phi)

    # choose e coprime to n and 1 > e > phi
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    print("e:\n", e)
    print("phi:\n", phi)
    # d[1] = modular inverse of e and phi
    d = euler_totient(e, phi)[1]

    # make sure d is positive
    d = d % phi
    if d < 0:
        d += phi

    return ((e, n), (d, n))


# function used for decryption
def decrypt(ciphertext, private_key):
    try:
        key, n = private_key
        text = [chr(pow(char, key, n)) for char in ciphertext]
        return "".join(text)
    except TypeError as e:
        print(e)


# function used for encryption
def encrypt(text, public_key):
    key, n = public_key
    ciphertext = [pow(ord(char), key, n) for char in text]
    return ciphertext


# main function
def main():

    public_key, private_key = generate_key_pair()
    text = str(input("Enter the text you want to be encrypted with RSA: "))

    print("Public Key: ", public_key, "\n")
    print("Private Key: ", private_key, "\n")

    ciphertext = encrypt(text, public_key)
    plaintext = decrypt(ciphertext, private_key)

    print("Encrypted Text =", ciphertext, "\n")
    print("Decrypted Text =", plaintext, "\n")


if __name__ == "__main__":
    main()
