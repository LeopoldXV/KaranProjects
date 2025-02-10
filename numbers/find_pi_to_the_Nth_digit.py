from math import pi

def main(LIMIT, decimals):
    print(f'{pi:.{min(LIMIT, decimals)}f}')


if __name__=="__main__":
    LIMIT = 20
    decimals = int(input("Enter number of decimal places for pi: "))
    main(LIMIT, decimals)