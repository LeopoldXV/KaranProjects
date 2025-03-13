VOWELS = ['a', 'e', 'i', 'o', 'u']


def main(word):
    d = {}
    for c in word:
        if c in VOWELS:
            d[c] = d.get(c, 0) + 1

    print(f'Vowels: {d}')


if __name__ == "__main__":
    main(input('Word to counter vowels of: '))
