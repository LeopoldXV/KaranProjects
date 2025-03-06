def main():
    demonstrate_addition()

def demonstrate_addition():
    print('Addition of 2 complex numbers: a + b = (ax + ai) + (bx + bi) = (ax + bx) + (ai + bi)')
    print(f'E.g.: ', end='')
    print(add_complex('5+6i', '2-4i'))
    print('Subtraction of 2 complex numbers: a - b = (ax + ai) - (bx + bi) = (ax - bx) + (ai - bi)')
    print(f'E.g.: ', end='')
    print(subtract_complex('5+6i', '2-4i'))
    print('Multiplication of 2 complex numbers: (a+bi)(c+di)=(ac−bd)+(ad+bc)i')
    print(multiply_complex('4+3i', '2-5i'))
    print('Division of 2 complex numbers: a1a2=(ac+bd)/(c^2+d^2)+i[(bc−ad)/(c2+d2)]')
    print(divide_complex('2+5i', '4-1i'))

def add_complex(first, second):
    print(f'{first} + {second} = ', end='')
    first_real = int(first.split('+')[0]) if '+' in first else int(+first.split('-')[0])
    first_imaginary = int(first.split('+')[1].replace('i', '')) if '+' in first else int('-'+first.split('-')[1].replace('i',''))
    second_real = int(second.split('+')[0]) if '+' in second else int(second.split('-')[0])
    second_imaginary = int(second.split('+')[1].replace('i','')) if '+' in second else int('-'+second.split('-')[1].replace('i',''))

    return f'{(first_real + second_real)} + {(first_imaginary + second_imaginary)}i'

def subtract_complex(first, second):
    print(f'{first} - {second} = ', end='')
    first_real = int(first.split('+')[0]) if '+' in first else int(first.split('-')[0])
    first_imaginary = int(first.split('+')[1].replace('i', '')) if '+' in first else int(
        '-' + first.split('-')[1].replace('i', ''))
    second_real = int(second.split('+')[0]) if '+' in second else int(second.split('-')[0])
    second_imaginary = int(second.split('+')[1].replace('i', '')) if '+' in second else int(
        '-' + second.split('-')[1].replace('i', ''))

    return f'{(first_real - second_real)} + {(first_imaginary - second_imaginary)}i'

def multiply_complex(first, second):
    print(f'{first} * {second} = ', end='')
    first_real = int(first.split('+')[0]) if '+' in first else int(first.split('-')[0])
    first_imaginary = int(first.split('+')[1].replace('i', '')) if '+' in first else int(
        '-' + first.split('-')[1].replace('i', ''))
    second_real = int(second.split('+')[0]) if '+' in second else int(second.split('-')[0])
    second_imaginary = int(second.split('+')[1].replace('i', '')) if '+' in second else int(
        '-' + second.split('-')[1].replace('i', ''))

    return (f'{(first_real * second_real - first_imaginary * second_imaginary)}'
            f'+{(first_real * second_imaginary + first_imaginary * second_real)}i')

def divide_complex(first, second):
    print(f'{first} / {second} = ', end='')
    a = int(first.split('+')[0]) if '+' in first else int(first.split('-')[0])
    b = int(first.split('+')[1].replace('i', '')) if '+' in first else int(
        '-' + first.split('-')[1].replace('i', ''))
    c = int(second.split('+')[0]) if '+' in second else int(second.split('-')[0])
    d = int(second.split('+')[1].replace('i', '')) if '+' in second else int(
        '-' + second.split('-')[1].replace('i', ''))

    return f'{a * c + b * d}/{pow(c, 2) + pow(d, 2)} + i*{b * c - a * d}/{pow(c, 2) + pow(d, 2)}'


if __name__ == "__main__":
    main()