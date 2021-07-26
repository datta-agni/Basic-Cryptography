import base64


def encode_decode():
    print("1 to encode and 2 to decode")
    choice = int(input())
    enter = input().encode('utf-8')
    if (choice == 1):
        enter = base64.b64encode(enter)
        base64_encoded = enter.decode("utf-8")
        print(f"Encoded string: {base64_encoded}")
    elif (choice == 2):
        enter = base64.b64decode(enter)
        base64_decoded = enter.decode("utf-8")

        print(f"Decoded string: {base64_decoded}")
    else:
        quit()


if __name__ == "__main__":
    encode_decode()
