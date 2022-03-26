# k = 0
# for i in range(len(s)-1):
#     if s[i].isdigit():
#         k += 1
#     else:
#         j = s[i]
# print(j)

# Функция принимает арифметическое выражение в качестве аргумента и выводит результат этого выражения.
def znak(s):
    for i in range(len(s)):
        if s[i].isdigit():
            continue
        elif (s[i] == '*') and (s[i-1] == '*'):
            j = '**'
        else:
            j = s[i]
    if j == '+':
        return int(s.split(j)[0]) + int(s.split(j)[1])
    elif j == '-':
        return int(s.split(j)[0]) - int(s.split(j)[1])
    elif j == '/':
        return int(s.split(j)[0]) / int(s.split(j)[1])
    elif j == '%':
        return int(s.split(j)[0]) / 100
    elif j == '**':
        if len(s.split(j)[1]) == 0:
            return int(s.split(j)[0]) * int(s.split(j)[0])
        else:
            return int(s.split(j)[0]) ** int(s.split(j)[1])
    elif j == '*':
        return int(s.split(j)[0]) * int(s.split(j)[1])
print("Input operation:")
str = input()
print(znak(str))