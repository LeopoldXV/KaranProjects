def main(limit):
    first = 0
    second = 1
    print(first,end=' ')
    print(second,end=' ')
    third = first + second
    while third < limit:
        print(third, end=' ')
        first = second
        second = third
        third = first + second


if __name__=="__main__":
    NTH_NUMBER = 1000
    limit = int(input("Enter the limit of Fibonacci sequence: "))
    main(min(NTH_NUMBER, limit))