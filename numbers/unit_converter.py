def calculate(origin, target, value):
    if not is_valid(origin, target, value):
        print(f'Incorrect combo of {origin} {target} {value}')
    print(convert(origin, target, value))

def convert(origin, target, value):
    match origin:
        case 'usd':
            match target:
                case 'eur':
                    return float(value) * 0.966527
        case 'eur':
            match target:
                case 'usd':
                    return float(value) * 1.0346324
        case 'seconds':
            match target:
                case 'minutes':
                    return float(value) / 60
        case 'minutes':
            match target:
                case 'seconds':
                    return float(value) * 60


def is_valid(origin, target, value):
    if (origin and target not in ['eur', 'usd']) and (origin and target not in ['seconds', 'minutes']):
        return False
    if float(value) < 0:
        return False
    return True


if __name__ == "__main__":
    # just did time and currency, lazy one at that - too many combinations
    while True:
        type_of_unit_origin = input('Please enter the type of unit being converted (eur/usd/seconds/minutes/hours/days/months/years): ')
        type_of_unit_target = input('Please enter the type of unit you want to convert to (eur/usd/seconds/minutes/hours/days/months/years): ')
        value = input('Please enter the value of the unit: ')
        calculate(type_of_unit_origin, type_of_unit_target, value)