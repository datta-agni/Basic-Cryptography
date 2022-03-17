import math
"""
Used for ceiling function
"""


def encrypt_decrypt() -> None:
    key = (
        input("Enter keyword text (Contains unique letters only): "
              ).lower().replace(" ", "")
        )
    plain_text = input("Enter plain text (Letters only): ").lower().replace(
        " ", ""
        )

    length_key = len(key)
    length_plaintext = len(plain_text)
    row = int(math.ceil(length_plaintext / length_key))
    matrix = [["X"] * length_key for _ in range(row)]

    # print(matrix)
    t = 0
    for r in range(row):
        for c, charecter in enumerate(plain_text[t:t + length_key]):
            matrix[r][c] = charecter
        t += length_key

    # print(matrix)
    # to make alphabetically order of chars
    sort_order = sorted([(charecter, i) for i, charecter in enumerate(key)])
    # print(sort_order)

    cipher_text = ""
    for charecter, c in sort_order:
        for r in range(row):
            cipher_text += matrix[r][c]

    print("Encryption")
    print("Plaintext is :", plain_text)
    print("Ciphertext is :", cipher_text)

    matrix_new = [["X"] * length_key for _ in range(row)]
    # to make original key order when we know keyword
    key_order = [key.index(charecter) for charecter in sorted(list(key))]
    # print(key_order)

    t = 0
    for c in key_order:
        for r, charecter in enumerate(cipher_text[t:t + row]):
            matrix_new[r][c] = charecter
        t += row
    # print(matrix_new)

    p_text = ""
    for r in range(row):
        for c in range(length_key):
            p_text += matrix_new[r][c] if matrix_new[r][c] != "X" else ""

    print("Decryption")
    print("Ciphertext is :", cipher_text)
    print("Plaintext is :", p_text)


if __name__ == "__main__":
    encrypt_decrypt()
