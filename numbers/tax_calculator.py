def main():
    salary = float(input('Please enter gross salary (bruto I): '))
    print('Assuming:\nPlace of residence: Zagreb (23.6%/35.4%)\nNumber of children:0\nNumber of dependents:0')
    print(f'Net salary: {gross_1_to_net(salary)}')
    print(f'You are indirectly paying {round(salary * 1.165 - salary, 2)} for health care this month')

def gross_1_to_net(salary):
    doprinos_prvi_mirovinski_stup = salary * 0.15
    doprinos_drugi_mirovinski_stup = salary * 0.05
    ukupni_doprinosi_iz_bruta = doprinos_prvi_mirovinski_stup + doprinos_drugi_mirovinski_stup
    dohodak = salary - ukupni_doprinosi_iz_bruta
    OLAKSICA = 600
    POREZNA_OSNOVICA_STOPA = 0.236 # Zagreb
    porezna_osnovica = dohodak - OLAKSICA
    porez = porezna_osnovica * POREZNA_OSNOVICA_STOPA

    return round(salary - ukupni_doprinosi_iz_bruta - porez, 2)


if __name__ == "__main__":
    # implemented Croatian Gross (1) to Net salary calculator (tax is x1.25 so like...)
    main()