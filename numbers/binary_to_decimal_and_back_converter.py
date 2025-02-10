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
        whole_part = int(number)
        decimal_part = int(str(number).split('.')[1])



if __name__ == "__main__":
    direction = input("Which number are you converting, binary or decimal? b/d ")
    number = input("The number is: ")
    print(f"Can't convert, direction {direction} not valid, use b or d") \
        if (direction != 'b' and direction != 'd') \
        else main(direction, int(number) if direction == 'b' else float(number))