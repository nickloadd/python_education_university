# Task 1
# s = "Abracadabra"
# 2 print(s[len(s)-2])
# 3 первые пять
# print(s[0:5])

# 4 Вывести строку, кроме последних двух символов.
# print(s[0:(len(s)-2)])

# 5 Вывести все символы с четными индексами (считайте, что 0 - четный индекс)
# for i in range(0, len(s)):
#     if i%2 == 0:
#         print(s[i], end="")
#     else:
#         continue

# 6 Вывести все символы с нечетными индексами
# for i in range(0, len(s)):
#     if i%2 == 0:
#         continue
#     else:
#         print(s[i], end="")

# 7 Вывести все символы в обратном порядке
# i = len(s)
# while i:
#     print(s[i-1], end="")
#     i -= 1

# 8 Вывести все символы строки через один в обратном порядке, начиная с последнего
# i = len(s)
# while i:
#     if i%2 != 0:
#         print(s[i-1], end="")
#         i -= 1
#     else:
#         i -= 1
#         continue

# 9 Вывести длину данной строки.
# print("lenght=",len(s))

# Task 2
# Напишите код, который обрабатывает строковые данные и возвращает их с первыми заглавными буквами в каждом слове.

# 1-й вариант
# s = input()
# for i in s.split():
#     g = ''.join(i[0].upper() + i[1:])
#     print(g, end=" ")

# 2-й вариант
# g = s.split()
# g = ' '.join(word[0].upper() + word[1:] for word in s.split())

# Task 3
# Проверка на длина составляет не менее 12 символов, при этом он должен содержать хотя бы одну заглавную букву, хотя бы одну строчную букву, хотя бы одну цифру и хотя бы один спецсимвол.
s = input()
d = 0
a_little = 0 # счетчик для мал. букв
a_big = 0 # счетчик для бол. букв
symbol = 0 # счетчик для символов
z = 0 # счетчик для запреш. символов
c = " !@#$%^&*()-+" # массив символов
c_ban = " =_<>.,`~"
for i in range(0, len(s)):
    if s[i].isdigit():
        d += 1
    elif s[i].isalpha() and s[i].islower():
        a_little += 1
    elif s[i].isalpha() and s[i].isupper():
        a_big += 1
    elif c.find(s[i]):
        symbol += 1
    elif c_ban.find(s[i]):
        z += 1
print("z= ",z)
if z != 0:
    print("Ошибка! Запрещенный спецсимвол")
else:
    if len(s) >= 12 and ((d+a_big+a_little+symbol) >= 4):
        print("Сильный пароль")
    else:
        print("Рекомендации:")
        if len(s) < 12:
            print("Необходимо добавить", 12-len(s),"символов")
        if d == 0:
            print("Необходимо добавить цифру")
        if a_little == 0:
            print("Необходимо добавить строчную букву")
        if a_big == 0:
            print("Необходимо добавить заглавную букву")
        if symbol == 0:
            print("Необходимо добавить спецсимвол")


