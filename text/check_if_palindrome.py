def main(word):
    word = word.lower()
    mid = len(word) // 2
    palindrome = True
    for i in range(0, mid):
        if word[i] != word[len(word)-1-i]:
            palindrome = False
            break

    print(f'Palindrome={palindrome}')

if __name__ == "__main__":
    main(input('Word: '))
