# basic implementation of Rivest–Shamir–Adleman algorithm
"""Used for generating random numbers used for prime checking"""
import random
"""
Returns a non-negative Python integer with k random bits. This method is supplied with the MersenneTwister Generator
"""
maximum_prime_length = int(
    input(
        """
        Enter the number of bits for generation.
        It should be above 128bits.
        ENTER : """
        )
    )


def modular_inverse(number1, number2) -> tuple:
    """calculates the modular inverse from e and phi"""
    if number1 == 0:
        return (number2, 0, 1)
    else:
        g, y, x = modular_inverse(number2 % number1, number1)
        return (g, x - (number2 // number1) * y, y)


def gcd(number1, number2) -> int:
    """calculates the gcd of two integers"""
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def try_composite(a, d, n, s) -> bool:
    """check composite number for rabin-miller primality test"""
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    """n is definitely composite"""
    return True


def is_prime(n, precision_for_huge_n=16) -> bool:
    """checks if a number is a prime through miller-rabin primality test"""
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
        return not any(
            try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17)
            )
    """otherwise"""
    return not any(
        try_composite(a, d, n, s) for a in known_primes[:precision_for_huge_n]
        )


known_primes = [2, 3]
known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def generate_random_prime() -> int:
    """
    function used to generate random number which inturn are checked for being prime
    """
    while 1:
        random_prime = random.getrandbits(maximum_prime_length)
        if is_prime(random_prime):
            return random_prime


def generate_key_pair() -> tuple:
    """
    function used to generate the public-key, private-key pair
    """
    """generates to random primes for 'p' and 'q'"""
    p = generate_random_prime()
    q = generate_random_prime()
    n = p * q
    """phi(n) = phi(p) * phi(q)"""
    phi = (p - 1) * (q - 1)
    print("n:" + "\n" + str(n) + "\n" + "\n" + "phi:" + "\n" + str(phi) + "\n")
    """choose e coprime to n and 1 > e > phi"""
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    """d[1] = modular inverse of e and phi"""
    d = modular_inverse(e, phi)[1]
    """make sure d is positive"""
    d = d % phi
    if d < 0:
        d += phi

    return ((e, n), (d, n))


def decrypt(ciphertext, private_key):
    """function used for decryption"""
    try:
        key, n = private_key
        text = [chr(pow(char, key, n)) for char in ciphertext]
        return "".join(text)
    except TypeError as e:
        print(e)


def encrypt(text, public_key) -> list:
    """function used for encryption"""
    key, n = public_key
    ciphertext = [pow(ord(char), key, n) for char in text]
    return ciphertext


"""main function"""
if __name__ == "__main__":
    public_key, private_key = generate_key_pair()
    text = str(input("Enter the text you want to be encrypted with RSA: "))
    ciphertext = encrypt(str(text.encode("utf-8")), public_key)
    plaintext = decrypt(ciphertext, private_key)

    print(
        "Public Key: " + str(public_key) + "\n" + "\n" + "Private Key: " +
        "\n" + "\n" + str(private_key) + "\n" + "\n" + "Encrypted Text: " +
        "\n" + "\n" + str(ciphertext) + "\n" + "\n" + "Decrypted Text: " +
        "\n" + "\n" + str(plaintext)
        )
