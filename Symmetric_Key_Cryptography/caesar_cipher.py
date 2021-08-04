from string import ascii_letters
from typing import Dict, Optional


def encrypt(input_string: str,
            key: int,
            alphabet: Optional[str] = None) -> str:
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters

    # The final result string
    result = ""

    for character in input_string:
        if character not in alpha:
            # Append without encryption if character is not in the alphabet
            result += character
        else:
            # Get the index of the new key and make sure it isn't too large
            new_key = (alpha.index(character) + key) % len(alpha)

            # Append the encoded character to the alphabet
            result += alpha[new_key]

    return result


def decrypt(input_string: str,
            key: int,
            alphabet: Optional[str] = None) -> str:
    # Turn on decode mode by making the key negative
    key *= -1

    return encrypt(input_string, key, alphabet)


def brute_force(input_string: str,
                alphabet: Optional[str] = None) -> Dict[int, str]:
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters

    # To store data on all the combinations
    brute_force_data = {}

    # Cycle through each combination
    for key in range(1, len(alpha) + 1):
        # Decrypt the message and store the result in the data
        brute_force_data[key] = decrypt(input_string, key, alpha)

    return brute_force_data


def main():
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrypt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")

        # get user input
        choice = input("\nWhat would you like to do?: ").strip() or "4"

        # run functions based on what the user chose
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(encrypt(input_string, key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force_data = brute_force(input_string)

            for key, value in brute_force_data.items():
                print(f"Key: {key} | Message: {value}")

        elif choice == "4":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
