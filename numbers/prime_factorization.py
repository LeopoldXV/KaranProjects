def main(number):
    if not number.isdigit() or int(number) == 1:
        print("Number has no prime factors!")

    number = int(number)
    prime_factors = list()

    prime = 2
    primes = list()
    while number != 1:
        primes.append(prime)
        if number % prime == 0:
            prime_factors.append(prime)
            number //= prime
        else:
            # get next prime - to do that, have to first check whether it's divisible by any of the previous primes
            while True and prime < number:
                prime += 1
                is_prime = True
                for n in primes:
                    if prime % n == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(prime)
                    break

    print(prime_factors) if prime_factors else "Number has no prime factors!"



if __name__ == "__main__":
    main(input("Please enter a number: "))
