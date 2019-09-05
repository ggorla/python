try:
    age = int(input('Age :'))
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be 0')
