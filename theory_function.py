# def sum(x, y):
#     return x + y
# print(sum(34, 12))

# def solve(s):
#     c = []
#     for i in range(len(s)-1):
#         if i == 0 or i%2 == 0:
#             c.append(s[i])
#     return c
# # вызываем функцию solve с заданными параметрами и выводим результат ее работы
# print(solve([1, 2, 3, 4, 5, 6, 7, 8]))

# лямбда-функция - особые, анонимные функции, имеющие ряд ограничений, по сравнению с обычными функциями. Они локально решают единственную задачу.
# #ex.1
# def search_len(x):
#     return len(x)
# #ex. 2 (lambda)
# result = lambda x: len(x)

# Обычно, лямбда-функции применяют при вызове функций, которые в качестве аргументов содержат функции. Проблема использования лямбда-функций состоит в том, что иногда усложняется читаемость кода.
# func = lambda x, y: x + y
# func(1, 2)
# # result: 3
# func('a', 'b')
# # result: ab
# (lambda x,y: x + y)(1,2)
# #result: 3
# (lambda x,y: x + y)('a','b')
# # result: 'ab'

# Лямбда-функции не имеют имени, поэтому могут возникать проблемы с отловом ошибки. В рамках данного курса мы не будем более подробно останавливаться на данном виде функций и рекомендуем использовать стандартный, более явный тип.

# Функции могут принимать произвольное количество аргументов, для этого необходимо поставить символ * перед именем аргумента функции
# def func(*args):
#     return args
# print(func (1 , 2, 3, 'abc'))
# Также можно принимать аргументы в виде словаря, для этого необходимо использовать символ **
# def func(**kwargs):
#     return kwargs
# print(func(a=1, b=2, c=3))

def solve(s):
    ''' Функция solve принимает список
     создает пустой список
     находит элементы с четным индексом (включая 0)
     заносит их в созданный список и возвращает его'''
    #assert - отлов исключений
    assert type(s) == list
    c = []
    for i in range(len(s)):
        if i == 0 or i % 2 == 0:
            c.append(s[i])
    return c


print(solve([0, 1, 2, 3, 4]))
