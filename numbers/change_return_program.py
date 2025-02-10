def main(cost, money_given):
    if (money_given < cost):
        print(f"User did give not enough money, {cost-money_given} more needed!")
        return

    NICKLE = 5
    DIME = 10
    QUARTER = 25
    remaining = round(((money_given - cost) - int(money_given - cost)), 2) * 100
    print(f"Base change: {int(money_given - cost)}")
    print(f"Quarters: {int(remaining // QUARTER)}")
    remaining = remaining % QUARTER if remaining >= QUARTER else remaining
    print(f"Dimes: {int(remaining // DIME)}")
    remaining = remaining % DIME if remaining >= DIME else remaining
    print(f"Nickles: {int(remaining // NICKLE)}")
    remaining = remaining % NICKLE if remaining >= NICKLE else remaining
    print(f"Pennies: {int(remaining)}")


if __name__ == "__main__":
    COST = float(input("How much does the item cost? "))
    MONEY_GIVEN = float(input("How much money did the customer give? "))
    main(COST, MONEY_GIVEN)