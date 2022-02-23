key = input("Enter key: ")
key = key.replace(" ", "")
key = key.upper()


def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]


"""Starting initialization"""
k = 0
flag = 0
result = list()
# storing the key
for c in key:
    if c not in result:
        if c == "J":
            result.append("I")
        else:
            result.append(c)

# storing the other available characters
for i in range(65, 91):
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))

# initialize matrix
matrix = matrix(5, 5, 0)
# making matrix
for i in range(0, 5):
    for j in range(0, 5):
        matrix[i][j] = result[k]
        k += 1
"""Ending initialization"""


# get location of each character
def locindex(c):
    location = list()
    if c == "J":
        c = "I"
    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if c == l:
                location.append(i)
                location.append(k)
                return location


# Encryption
def encrypt():
    message = str(input("ENTER MESSAGE: "))
    message = message.upper()
    message = message.replace(" ", "")
    i = 0
    for s in range(0, len(message) + 1, 2):
        if s < len(message) - 1:
            if message[s] == message[s + 1]:
                message = message[:s + 1] + "X" + message[s + 1:]
    if len(message) % 2 != 0:
        message = message[:] + "X"
    print("CIPHER TEXT:", end=" ")
    while i < len(message):
        location = list()
        location = locindex(message[i])
        location1 = list()
        location1 = locindex(message[i + 1])
        if location[1] == location1[1]:
            print(
                "{}{}".format(
                    matrix[(location[0] + 1) % 5][location[1]],
                    matrix[(location1[0] + 1) % 5][location1[1]],
                    ),
                end=" ",
                )
        elif location[0] == location1[0]:
            print(
                "{}{}".format(
                    matrix[location[0]][(location[1] + 1) % 5],
                    matrix[location1[0]][(location1[1] + 1) % 5],
                    ),
                end=" ",
                )
        else:
            print(
                "{}{}".format(
                    matrix[location[0]][location1[1]],
                    matrix[location1[0]][location[1]],
                    ),
                end=" ",
                )
        i = i + 2


# decryption
def decrypt():
    message = str(input("ENTER CIPHERTEXT: "))
    message = message.upper()
    message = message.replace(" ", "")
    print("PLAINTEXT: ", end=" ")
    i = 0
    while i < len(message):
        location = list()
        location = locindex(message[i])
        location1 = list()
        location1 = locindex(message[i + 1])
        if location[1] == location1[1]:
            print(
                "{}{}".format(
                    matrix[(location[0] - 1) % 5][location[1]],
                    matrix[(location1[0] - 1) % 5][location1[1]],
                    ),
                end=" ",
                )
        elif location[0] == location1[0]:
            print(
                "{}{}".format(
                    matrix[location[0]][(location[1] - 1) % 5],
                    matrix[location1[0]][(location1[1] - 1) % 5],
                    ),
                end=" ",
                )
        else:
            print(
                "{}{}".format(
                    matrix[location[0]][location1[1]],
                    matrix[location1[0]][location[1]],
                    ),
                end=" ",
                )
        i = i + 2


while 1:
    choice = int(input("\n1.) Encryption: \n2.) Decryption: \n3.) Exit\n"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice!")
