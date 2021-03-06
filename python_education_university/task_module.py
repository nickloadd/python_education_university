# Task #3
# Проверка на длина составляет не менее 12 символов, при этом он должен содержать хотя бы одну заглавную букву, хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол.
# check password function
from random import *

def check(s):
    # global result
    d = 0  # счетчик для цифр цифр
    a_little = 0  # счетчик для мал. букв
    a_big = 0  # счетчик для бол. букв
    symbol = 0  # счетчик для символов
    z = 0  # счетчик для запреш. символов
    q = '!@#$%^&*()-+'  # массив символов

    for i in range(0, len(s)):  # цикл проверки пароля
        if s[i].isdigit():  # проверка на цифру
            d += 1
        elif s[i].isalpha() and s[i].islower():  # проверка на строчную букву
            a_little += 1
        elif s[i].isalpha() and s[i].isupper():  # проверка на пропискную букву
            a_big += 1
        elif q.find(s[i]) == -1:  # проверка на запрещенный символ
            z += 1
        elif q.find(s[i]) != -1:  # проверка на допустимый символ
            symbol += 1

    if z != 0:
        result = "Ошибка! Запрещенный спецсимвол"
    else:
        if len(s) >= 12 and ((d + a_big + a_little + symbol) >= 4):
            result = "Сильный пароль"
        else:
            result = "Рекомендации:\n"
            if len(s) < 12:
                result += "Необходимо добавить " + str(12 - len(s)) + " символов\n"
            if d == 0:
                result += "Необходимо добавить цифру\n"
            if a_little == 0:
                result += "Необходимо добавить строчную букву\n"
            if a_big == 0:
                result += "Необходимо добавить заглавную букву\n"
            if symbol == 0:
                result += "Необходимо добавить спецсимвол\n"
    return result

def generation_password():
    passw = ""
    case = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(randrange(4, 9)):
        passw += choice('!@#$%^&*()-+')
        passw += choice(case)
        passw += choice(case.upper())
        passw += str(randrange(0, 9, 1))
    return passw

# sk = input()
print(generation_password())
print(check(generation_password()))

