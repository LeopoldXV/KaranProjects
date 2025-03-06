def fast_exponentiation(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:  # If b is odd, multiply the current base
            result *= a
        a *= a  # Square the base
        b //= 2  # Reduce exponent by half
    return result


def main():
    a = int(input('First integer: '))
    b = int(input('Second integer: '))
    print(fast_exponentiation(a, b))


if __name__ == "__main__":
    main()
