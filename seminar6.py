# В модуль с проверкой даты!
# - добавьте возможность запуска в терминале с передачей даты на проверку.
import sys


def _leap_year (year):
    res = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        res = True
    return res


def my_date (date: str):
    check = False
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            check = True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            check = True
        elif month == 2:
            if _leap_year(year):
                if 1 <= day <= 29:
                    check = True
            else:
                if 1 <= day <= 28:
                    check = True
    res = f'Настоящий: {check}, високосный: {_leap_year(year)}'
    return res


if __name__ == '__main__':
    print(my_date(sys.argv[1]))


# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
# 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
#  каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. .

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import random
import time

from my_package import writer


def is_queen_beat (position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True  # ферзи не бьют
    else:
        return False  # ферзи бьют


def successful_position (count_successful):
    start = time.time()
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_successful:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if is_queen_beat(position):
            end = time.time()
            data = f' попытка: {count_iter}, затраченное время: {end - start}'
            writer.log(position, data)

            count += 1
        print(position)
        position.clear()