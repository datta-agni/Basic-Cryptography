# basic implementation of Rivest–Shamir–Adleman algorithm
"""
Used for generating random numbers used for prime checking
"""
import random


def modular_inverse(number1: int, number2: int) -> tuple[int, int, int]:
    """
    calculates the modular inverse from e and phi.
    """
    if number1 == 0:
        return (number2, 0, 1)
    else:
        g, y, x = modular_inverse(number2 % number1, number1)
        return g, x - (number2 // number1) * y, y


def gcd(number1: int, number2: int) -> int:
    """
    calculates the gcd of two integers.
    """
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def try_composite(a: int, d: int, n: int, s: int) -> bool:
    """
    check composite number for rabin-miller primality test.
    """
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    """
    n is definitely composite.
    """
    return True


def is_prime(n: int, precision_for_huge_n: int = 128) -> bool:
    """
    checks if a number is a prime through miller-rabin primality test.
    """
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


def generate_random_prime(maximum_prime_length: int) -> int:
    """
    Generate a prime.
    Args:
        length--int--length of the prime to generate in bits return a prime.
    """
    random_number_candidate: int = 4

    # keep generating while the primality test fail.
    while not is_prime(random_number_candidate, 128):
        random_number_candidate = random.getrandbits(maximum_prime_length)
    return random_number_candidate


def generate_key_pair() -> tuple[tuple[int, int], tuple[int, int]]:
    """
    function used to generate the public-key and private-key pair.
    """

    # Returns a non-negative Python integer with k random bits.
    # This method is supplied with the Mersenne Twister Generator.
    length = int(
        input(
            """
            \n
            Enter the number of bits for generation.
            It should be above 128bits.
            ENTER :
            \n
            """
            )
        )
    """
    generates to random primes for 'p' and 'q'
    """
    p = generate_random_prime(length)
    q = generate_random_prime(length)
    n = p * q
    """
    phi(n) = phi(p) * phi(q).
    """
    phi = (p - 1) * (q - 1)
    print("n:" + "\n" + str(n) + "\n\n" + "phi:" + "\n" + str(phi) + "\n")
    """
    choose e coprime to n and 1 > e > phi.
    """
    e = random.randint(1, phi)
    g = gcd(e, phi)

    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    """
    d[1] = modular inverse of e and phi.
    """
    d = modular_inverse(e, phi)[1]
    """
    make sure d is positive.
    """
    d = d % phi
    if d < 0:
        d += phi

    return (e, n), (d, n)


def decrypt(ciphertext: str, private_key: tuple[int, int]):
    """
    function used for decryption.
    """
    try:
        key, n = private_key
        text = [chr(pow(int(char), key, n)) for char in ciphertext]
        return "".join(text)
    except TypeError as e:
        print(e)


def encrypt(text: str, public_key: tuple[int, int]) -> str:
    """
    function used for encryption.
    """
    key, n = public_key
    ciphertext: str = str([pow(ord(char), key, n) for char in text])
    return ciphertext


# main function.
if __name__ == "__main__":
    public_key, private_key = generate_key_pair()
    text = str(input("Enter the text you want to be encrypted with RSA: "))
    ciphertext = encrypt(str(text.encode("utf-8")), public_key)
    plaintext = decrypt(ciphertext, private_key)

    print(
        "Public Key: " + str(public_key) + "\n\n" + "Private Key: " + "\n\n" +
        str(private_key) + "\n\n" + "Encrypted Text: " + "\n\n" +
        str(ciphertext) + "\n\n" + "Decrypted Text: " + "\n\n" +
        str(plaintext)
        )
