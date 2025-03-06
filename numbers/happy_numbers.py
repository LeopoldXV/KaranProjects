def main():
    happy = []
    num = 0

    while len(happy) < 8:
        if is_happy(num):
            happy.append(num)
        num += 1

    print(happy)


def is_happy(number):
    seen = {number}

    while True:
        squared_digits_sum = sum(list(map(lambda x: x * x, [int(d) for d in str(number)])))
        if squared_digits_sum == 1:
            return True
        if squared_digits_sum in seen:
            return False
        seen.add(squared_digits_sum)
        number = squared_digits_sum


if __name__ == "__main__":
    main()
