def main():
    number = 10 # for sanity's reason
    print(solve_with_for_loops(number))
    print(solve_with_recursion(number))

def solve_with_for_loops(limit):
    product = 1
    for i in range(0, limit+1):
        product = product * i if i > 0 else product
    return product

def solve_with_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * solve_with_recursion(n - 1)


if __name__ == "__main__":
    main()