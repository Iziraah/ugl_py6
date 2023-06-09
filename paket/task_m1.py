# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. .


date = input('Введите дату для проверки: ')

def calend(date):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
            
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            if 1 <= day <= 28 + leap_year(year):
                return True
    return False


def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# calend(date)