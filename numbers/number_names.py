def spell_number(number):
    ones = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10
    ten_thousands = number // 10000 % 10
    hundred_thousands = number // 100000 % 10
    millions = number // 1000000 % 10

    d = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: ''
    }

    d10 = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
        0: ''
    }

    d1x = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

    spoken_millions = d[millions] + ' million ' if millions != 0 else ''
    spoken_hundred_thousands = d[hundred_thousands] + ' hundred ' if hundred_thousands != 0 else ''
    if ten_thousands == 0:
        spoken_ten_thousands = ''
    elif ten_thousands == 1:
        spoken_ten_thousands = d1x[ten_thousands * 10 + thousands]
        spoken_thousands = ''
    else:
        spoken_ten_thousands = d10[ten_thousands]
    if ten_thousands != 1:
        spoken_thousands = d[thousands]

    thousand_word = ' thousand ' if hundred_thousands != 0 or ten_thousands != 0 or thousands != 0 else ''
    spoken_hundreds = d[hundreds] + ' hundred ' if hundreds != 0 else ''

    if tens == 0:
        spoken_tens = ''
    elif tens == 1:
        spoken_tens = d1x[tens * 10 + ones]
        spoken_ones = ''
    else:
        spoken_tens = d10[tens]
    if tens != 1:
        spoken_ones = d[ones]

    print(f'The number is: '
          f'{spoken_millions}{spoken_hundred_thousands}{spoken_ten_thousands}{spoken_thousands}{thousand_word}{spoken_hundreds}{spoken_tens}{spoken_ones}')


def main():
    number = input('Please input a whole number to spell: ')
    spell_number(int(number))


if __name__ == "__main__":
    # no optional support
    main()
