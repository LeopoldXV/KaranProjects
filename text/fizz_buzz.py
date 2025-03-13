def main():
    for i in range(1, 101, 1):
        if i % 15 == 0:
            print(f'{i} - FizzBuzz')
        elif i % 3 == 0:
            print(f'{i} - Fizz')
        elif i % 5 == 0:
            print(f'{i} - Buzz')
        else:
            print(i)


if __name__ == "__main__":
    main()
