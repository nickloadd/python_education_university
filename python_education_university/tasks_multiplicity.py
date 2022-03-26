# Task 1
# Дан список чисел. Напишите программу, которая определяет, сколько в нем встречается различных чисел, используя множества.

# # Ввод списка(массива)
# k = int(input('Length of list:'))
# l = []
# for i in range(0, k):
#     l.append(input())
# print(l)
# # Задаем множество
# a = set(l)
# # Вывод количества разных элементов
# print('Count different elem:', len(a))

# Task 2
# Даны два списка чисел. Напишите программу, которая определяет, сколько в них встречается общих чисел, используя множества.

# # 1st list
# # Ввод списка(массива)
# k1 = int(input('Length of list:'))
# l1 = []
# for i in range(0, k1):
#     l1.append(input())
# print(l1)
# # Задаем множество 1
# a = set(l1)
# # 2nd list
# k2 = int(input('Length of list:'))
# l2 = []
# for i in range(0, k2):
#     l2.append(input())
# print(l2)
# # Задаем множество 2
# b = set(l2)
# # intersection
# print(len(a.intersection(b)))

# Task 3
# Даны два множества чисел. Напишите программу, которая определяет, является ли первое множество подмножеством второго.
# Множество является подмножеством другого множества, если все данные первого совпадают с частью данных из второго. Если множества совпадают, они не являются подмножествами друг друга.

# 1st list
# Ввод списка(массива)
# k1 = int(input('Length of list:'))
# l1 = []
# for i in range(0, k1):
#     l1.append(input())
# print(l1)
# # Задаем множество 1
# a = set(l1)
# # 2nd list
# k2 = int(input('Length of list:'))
# l2 = []
# for i in range(0, k2):
#     l2.append(input())
# print(l2)
# # Задаем множество 2
# b = set(l2)
# # intersection
# if a.issubset(b) and len(a) != len(b):
#     print(True)
# else:
#     print(False)