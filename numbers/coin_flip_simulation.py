import random
def main():
    number_of_tosses = int(input('How many times do you want to simulate a coin toss? '))
    heads = 0
    tails = 0
    for _ in range(number_of_tosses):
        outcome = flip()
        print(f'Outcome is: {outcome}')
        if outcome == 'heads':
            heads += 1
        else:
            tails += 1
        print(f'So far, heads: {heads}, tails: {tails}')

def flip():
   return random.choice(['heads', 'tails'])


if __name__ == "__main__":
    main()