# Reverse string cipher


def rev_string_cipher(text):
    # function reverses the given string
    size = len(text) - 1
    encoded = ""
    # code to reverse the string given
    while size >= 0:
        encoded = encoded + text[size]
        size = size - 1

    print("The cipher text is :", encoded)


def main():
    # takes input
    message = str(input("ENTER A CIPHER TEXT: "))
    rev_string_cipher(message)


if __name__ == '__main__':
    main()
