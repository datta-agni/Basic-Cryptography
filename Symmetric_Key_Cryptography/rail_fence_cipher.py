# RailFence Cipher


def fence(lst, rail):
    fence = [[None] * len(lst) for n in range(rail)]
    rails = range(rail - 1) + range(rail - 1, 0, -1)
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0:               # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]


def encode(text, n):
    return ''.join(fence(text, n))


def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


def main():
    text = str(input('Enter the Plaintext: '))
    rail_level = int(input("Enter rails(level): "))
    z = encode(text, rail_level)
    print(z)
    y = decode(z, rail_level)
    print(y)


if __name__ == '__main__':
    main()
