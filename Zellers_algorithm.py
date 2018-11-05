def is_birthday():
    '''Calculate day of the birth.'''
    name = input('What is your name?\n')
    print()
    birth_year = int(input('Enter your birth year\n'))
    print()
    birth_month = int(input('Enter your birth month (from 1 to 12)\n'))
    print()
    birth_day = int(input('Enter your birth day\n'))
    print()

    day_of_the_week = ('Sanday', 'Monday', 'Tuesday', 'Wensday', 'Thursday', 'Friday', 'Satuday')

    if birth_month > 2:
        A = birth_month - 2
    else:
        A = birth_month + 10
        birth_year -= 1

    B = birth_day
    C = birth_year % 100
    D = birth_year // 100
    W = int((13 * A - 1) / 5)
    X = int(C / 4)
    Y = int(D / 4)
    Z = int(W + X + Y + B + C - 2 * D)
    R = int(Z % 7)

    if R < 0:
        R += 7

    return '{}, day of Your birth is {}!'.format(name, day_of_the_week[R])

day_of_your_birth = is_birthday()
print(day_of_your_birth)