# Implementation of Affine Cipher in Python


# Extended Euclidean Algorithm for finding modular inverse
def euclid_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


# modular inverse does not exist
def modinv(a, m):
    gcd, x, y = euclid_gcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


# affine ciphertext encryption function returns the ciphertext
def affine_encrypt(plaintext, key):
    """
    C = (a * P + b) % 26
    """
    return "".join([
        chr(((key[0] * (ord(t) - ord("A")) + key[1]) % 26) + ord("A"))
        for t in plaintext.upper().replace(" ", "")
        ])


# affine ciphertext decryption function returns original ciphertext
def affine_decrypt(ciphertext, key):
    """
    P = (a ^ ( -1 ) * ( C - b )) % 26
    """
    return "".join([
        chr(((modinv(key[0], 26) *
              (ord(charecter) - ord("A") - key[1])) % 26) + ord("A"))
        for charecter in ciphertext
        ])


def main():
    # declaring ciphertext and key
    message = str(input("Enter the message you want to encrypt: "))
    key1 = int(input("Enter the first half of the key of encryption: "))
    key2 = int(input("Enter the second half of the key of encryption: "))
    key = [key1, key2]

    # calling encryption function
    affine_encrypted_text = affine_encrypt(message, key)
    print("Encrypted Text: {}".format(affine_encrypted_text))

    # calling decryption function
    print(
        "Decrypted Text: {}".format(
            affine_decrypt(affine_encrypted_text, key)
            )
        )


if __name__ == "__main__":
    main()
