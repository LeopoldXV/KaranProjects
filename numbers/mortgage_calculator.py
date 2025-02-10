def main(principle, term, interest_rate):
    print(f"calculating mortgage for loan of {principle}, term of {term} years and interest rate of {interest_rate}%")
    P = principle # loan amount in nominal currency
    I = interest_rate / 100 / 12 # monthly interest rate
    N = term * 12 # number of installments in months
    return P*I/(1 - pow(1 + I, -(N)))

if __name__ == "__main__":
    # no "added complexity" additional work done
    PRINCIPAL = 400000
    TERM = 30
    INTEREST_RATE = 5
    print(main(PRINCIPAL, TERM, INTEREST_RATE))