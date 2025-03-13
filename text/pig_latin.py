CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y']


def main(user_word):
    """
    My rules: just move all the consonants and put -ay, or move all vowels and put -way
    """
    word = user_word.lower()
    boundary = 0
    if word[0] in CONSONANTS:
        for i, c in enumerate(word):
            if c not in CONSONANTS:
                boundary = i
                break
        pig_latin_word = user_word[boundary:] + user_word[:boundary] + 'ay'
    else:
        pig_latin_word = user_word + 'way'

    print(pig_latin_word)


if __name__ == "__main__":
    main(input('Word to Pig Latin-ify: '))
