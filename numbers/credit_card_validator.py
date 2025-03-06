def main():
    cc_number = input('Please enter credit card number: ')  # "378282246310005" # e.g. valid amex
    if validate(cc_number):
        print(f'Credit card number {cc_number} is valid')
        return
    print(f'Credit card number {cc_number} is NOT valid')


def validate(cc_number):
    # Visa: 16 (4), MasterCard: 16 (5), American Express: 15 (3), Discoverer: 16 (6)
    if is_cc_number(cc_number) and is_cc_number_valid(int(cc_number)):
        return True
    return False


def is_check_digit_valid(num_list):
    check_digit = num_list.pop()
    total = luhn_sum(num_list)
    return check_digit == (10 - (total % 10)) % 10


def luhn_sum(num_list):
    num_list = num_list[::-1]
    for i, n in enumerate(num_list):
        if i % 2 == 0:
            num_list[i] = n * 2 if n * 2 <= 9 else (n * 2) - 9
    return sum(num_list)


def is_cc_number_valid(number):
    num_list = [int(n) for n in str(number)]
    match len(num_list):
        case 15:
            match num_list[0]:
                case 3:
                    return is_check_digit_valid(num_list)
                case _:
                    print(f'Amex card (15 digits), but leading digit {num_list[0]} is not amex (should be 3)!')
                    return False
        case 16:
            match num_list[0]:
                case 4 | 5 | 16:
                    return is_check_digit_valid(num_list)
                case _:
                    print(
                        f'Got a 16 digit CC number, but leading digit {num_list[0]} is not any of the known ones (4 Visa, 5 MasterCard, 6 Discover)!')
                    return False


def is_cc_number(cc_number):
    return cc_number.isdigit()


if __name__ == "__main__":
    main()
