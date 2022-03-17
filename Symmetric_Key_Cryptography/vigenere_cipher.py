# Vigenere encryption and decryption

from itertools import starmap, cycle


def encrypt(message: str, key: str) -> str:
    """
    Vigenere encryption of message using key.
    Converted to uppercase.
    Non-alpha characters stripped out.
    """

    message = str(filter(str.isalpha, message.upper()))

    def encode(c: str, k: str) -> str:
        # Single letter encryption.
        return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(encode, zip(message, cycle(key))))


def decrypt(message: str, key: str) -> str:
    """
    Vigenere decryption of message using key.
    """

    def decode(c: str, k: str) -> str:
        # Single letter decryption.
        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(decode, zip(message, cycle(key))))


def main() -> None:
    text = str(
        input("Enter a string to be encoded or decoded in Vigenere Cipher\n")
        )
    key = str(input("Enter the Vigenere Cipher Key:\n"))

    enc: str = encrypt(text, key)
    dec: str = decrypt(enc, key)

    print("Original Text: ", text)
    print("Encrypted Text: ", enc)
    print("Decrypted Text: ", dec)


if __name__ == '__main__':
    main()
