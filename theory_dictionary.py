d1 = dict(short='dict', long='dictionaty')
d2 = dict([(1,1), (2,4)])
d3 = {}
d4 = {'dict': 1, 'dictionary': 2}
d5 = dict.fromkeys(['a', 'b'])
d6 = dict.fromkeys(['a', 'b'], 100)
d7 = {a: a ** 2 for a in range(7)}
# clear() очищает словарь
d7.clear()
# copy() возврщает копию словаря
b = d7.copy()
# fromkeys(seq,[value]) создает словарь с ключами из seq  и значением value
d1.fromkeys(['a','b'], 10)
# get(key[,deafault]) возвращает значение ключа, но если его нет, то возвращает default
d8 = {'a': 1, 'b': 2}
d8.get('a')
# items() возвращает пары (ключ, значение)
d8.items()
# keys() возвращает ключи в словаре
print(d8.keys())
# pop(key[,default]) удаляет ключ и возвращает сзначение. Если ключа нет, возвращает default
d8.pop('a') # станет d8={'b':2}
# popintem() удааляет и возвращает пару (ключ, значение) с конца
d8.popitem() # станет d8={'a':1}
# setdefault(key[,default]) возвращает значение ключа, если его нет, то создает ключ с значением default
d9 = {'a': 1, 'b': 2}
d9.setdefault('e', 6)
# d9 = {'a': 1, 'b': 2, 'e': 6}
d9.setdefault('f')
# d9 = {'a': 1, 'b': 2, 'e': 6, 'f': None}

# update([other]) обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются
d10 = {'a': 1, 'b': 2}
d10.update({'d': 5})
#d10 = {'a': 1, 'b': 2, 'd': 5}

#values() возвращает значения в словаре
d10.values()