# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь. .

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

board = [[0 for i in range(8)] for j in range(8)]
count = 0
pozition = []


def SetQueen(i, j):
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i+j-x < 8:
            board[i+j-x][x] += 1
        if 0 <= i-j + x < 8:
            board[i-j + x][x] += 1
    board[i][j] = -1


def RemoveQueen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i+j-x < 8:
            board[i+j-x][x] -= 1
        if 0 <= i-j + x < 8:
            board[i-j + x][x] -= 1
    board[i][j] = 0


def printPozition():  # Выводит все возможные варианты расстановки
    global count
    count += 1
    abc = 'abcdefgh'
    ans = []
    # if count == 5:
    #     exit()
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i+1))
    print(', '.join(ans))


def solve(i):  # Выводит все возможные варианты расстановки, вызов
    for j in range(8):
        if board[i][j] == 0:
            SetQueen(i, j)
            if i == 7:
                printPozition()
            else:
                solve(i+1)
            RemoveQueen(i, j)


def arrPoz():  # будет генерить список всех возможных расстановок
    global count
    vers = []
    count += 1
    ans = []
    abc = 'abcdefgh'
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i+1))
    # print(', '.join(ans))
    if ans:
        vers.append(ans)
    return vers


versions = []


def solve2(i):  # будет генерить список всех возможных расстановок, вызов
    global versions
    for j in range(8):
        if board[i][j] == 0:
            SetQueen(i, j)
            if i == 7:
                versions.append(arrPoz())
            else:
                solve2(i+1)
            RemoveQueen(i, j)







def findVar():  # проверяет вхождение введенного варианта
    enterVariant = input(
    "Введите предполагаемое расположение ферзей, через пробел,\n вида a2, f4 и т.д.: ")
    yourVariant = [enterVariant.split()]
    if yourVariant in versions:
        print("yes")
    else:
        print("no")


