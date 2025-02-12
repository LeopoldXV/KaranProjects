def main(direction, number):
    if direction == 'b':
        multiplier = 0
        decimal = 0
        while number > 0:
            decimal += (number % 10) * pow(2, multiplier)
            multiplier += 1
            number //= 10
        print(f'{number} converted to decimal is {decimal}')
    else:
        final = []
        whole_part = abs(int(number))
        while whole_part != 0:
            final.append(whole_part % 2)
            whole_part //= 2
        final = final[::-1]
        decimal_part = float('.'+str(number).split('.')[1])
        if decimal_part == 0:
            print(''.join([str(n) for n in final]))
            return
        final.append('.')
        seen = set()
        while True:
            part = decimal_part * 2
            final.append(1 if part >= 1 else 0)
            if part in seen or part == 1.0:
                break
            else:
                seen.add(part)
            if part > 1:
                decimal_part = part - 1
            else:
                decimal_part = part
        print(f"Number {number} is {''.join([str(n) for n in final])} in binary")



if __name__ == "__main__":
    direction = input("Which number are you converting, binary or decimal? b/d ")
    number = input("The number is: ")
    print(f"Can't convert, direction {direction} not valid, use b or d") \
        if (direction != 'b' and direction != 'd') \
        else main(direction, int(number) if direction == 'b' else float(number))