def main():
    prime = 2
    primes = [prime]

    while True:
        next_one =  input("Generate next prime? y/n ")
        if next_one == "n":
            break
        elif next_one != "y":
            print("Please specify y for yes or n for no")
            continue
        else:
            print(prime)
        # get next prime
        while True:
            prime += 1
            is_prime = True
            for n in primes:
                if prime % n == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(prime)
                break


if __name__ == "__main__":
    main()
