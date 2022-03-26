# Task 1
# Задан список с числами. Напишите программу, которая выводит все элементы списка с четными индексами в виде нового списка.

# print("Len of list:")
# k = int(input())
# # print(k)
# l = []
# j = []
# for i in range(0, k):
#     l.append(input())
# print(l)
# for i in range(0, k):
#     if i%2 ==0:
#         j.append(l[i])
# print(j)

# Task 2
# Задан список с числами. Напишите программу, которая выводит все элементы списка, которые больше предыдущего, в виде отдельного списка.

# print("Len of list:")
# k = int(input())
# # print(k)
# l = []
# j = []
# for i in range(0, k):
#     l.append(input())
# print(l)
# for i in range(1, k):
#     if l[i]>l[i-1]:
#         j.append(l[i])
# print(j)

# Task 3
# Задан список с числами. Напишите программу, которая меняет местами наибольший и наименьший элемент и выводит новый список.

print("Len of list:")
k = int(input())
# a = 0
# b = 0
# print(k)
l = []
j = []
for i in range(0, k):
    l.append(input())
print(l)
for i in range(1, k):
    if l[i]>l[i-1]:
        j.append(l[i])
        j.append(l[i-1])
    else:
        j.append(l[i-1])
    # j.append(l[i])
# j.reverse()
print(j)

#This some changes for my project