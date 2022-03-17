# ROT13 cipher


def dencrypt(message: str, n: int = 13) -> str:
    output_text = ""
    for charecter in message:
        if "A" <= charecter <= "Z":
            output_text += chr(ord("A") + (ord(charecter) - ord("A") + n) % 26)
        elif "a" <= charecter <= "z":
            output_text += chr(ord("a") + (ord(charecter) - ord("a") + n) % 26)
        else:
            output_text += charecter
    return output_text


def main() -> None:
    plaintext = input("Enter message: ")
    ciphertext = dencrypt(plaintext, 13)
    print("Encryption:", ciphertext)

    plaintext = dencrypt(ciphertext, 13)
    print("Decryption: ", plaintext)


if __name__ == "__main__":
    main()
