def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('not leap year.')
        else:
            print('Leap Year')

    else:
        print('Not a Leap year.')


is_leap(2400)
