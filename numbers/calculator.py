def calculate(first, second, operand):
    if operand == '*':
        return first * second
    elif operand == '/':
        return first / second
    elif operand == '+':
        return first + second
    else:
        return first - second

def is_number(user_input):
    return user_input.replace('.', '', 2).isdigit()

def is_operand(user_input):
    return user_input in ['*', '/', '+', '-']



if __name__ == "__main__":
    # no added complexity implemented (not a scientific calculator)
    # also pretty dumb, based on FIRST, OPERAND, SECOND inputs
    first = None
    operand = None
    while True:
        user_input = input('Input ')
        if not is_number(user_input) and not is_operand(user_input):
            print("Please enter a number of a mathematical operation ")
        if is_number(user_input):
            if operand is not None and first is not None:
                result = calculate(first, float(user_input), operand)
                print(result)
                first = float(result)
                operand = None
            elif operand is None:
                first = float(user_input)
        if is_operand(user_input):
            operand = user_input

