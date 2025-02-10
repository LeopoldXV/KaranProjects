from math import e

def main(LIMIT, decimals):
    print(f'{e:.{min(LIMIT, decimals)}f}')


if __name__=="__main__":
    LIMIT = 20
    decimals = int(input("Enter number of decimal places for e: "))
    main(LIMIT, decimals)