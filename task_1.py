import leap_check
from sys import argv

__all__ = ['check_date_format', 'check_date']


def check_date_format(date):
    if len(date) == 10:
        if date[2] and date[5] == ".":
            digits = date[:2] + date[3:5] + date[6:]
            if digits.isdigit():
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_date(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
        if month == 2:
            if leap_check._leap_year_check(year):
                if day <= 29:
                    return True
                else:
                    return False
            else:
                if day <= 28:
                    return True
                else:
                    return False
        elif month in (4, 6, 9, 11):
            if day <= 30:
                return True
            else:
                return False
        return True
    else:
        return False


while True:
    # input_date = input("Введите дату: ")
    input_date = argv[1]
    if check_date_format(input_date):
        if check_date(input_date):
            print("Вы ввели возможную дату.")
            break
        else:
            print("Вы ввели невозможную дату. Попробуйте снова.")
    else:
        print("Вы ввели данные в неправильном формате. Попробуйте снова.")
