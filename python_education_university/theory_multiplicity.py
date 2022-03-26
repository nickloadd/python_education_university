##### Создание множества(неповторяющиеся данные в произвольном порядке)
#1
a = set()
print(a)
# Result: set()

#2
a = set('hello')
print(a)
# Result: {'h', 'o', 'l', 'e'}

#3
a = {'a', 'b', 'c', 'd'}
print(a)
# Result: {'b', 'c', 'a', 'd'}

#4
a = {i ** 2 for i in range(10)}
print(a)
# Result: {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

#Множества удобно использовать для удаления повторяющихся элементов:
words = ['hello', 'daddy', 'hello', 'mum']
set(words)
# Result: {'hello', 'daddy', 'mum'}

##### Methods of work with multiplicity
# len(s) - число элементов в множестве (размер множетсва)
a = {'a', 'b', 'c', 'd'}
len(a)
# Result: 4

# x in s - принадлежит ли х множеству s
a = {'a', 'b', 'c', 'd'}
'a' in a
# Result: True

# isdisjoint(other) - истина, если set и other НЕ имеют общих элементов
a = {'a', 'b', 'c', 'd'}
a.isdisjoint('a')
# Result: False
a.isdisjoint('f')
# Result: True

# issubset(other) или set<=other - истина, если все элементы set принадлжеат other
a = {'a', 'b', 'c', 'd'}
a.issubset({'a', 'b', 'c', 'd','f','e'})
# Result: True

# issuperset(other) или set >= other - аналогично (все элементы other принадлжеат set)

# union(other, ...) или set | other | ... - возвращает объединение нескольких множеств
a = {'a', 'b', 'c', 'd'}
a.union({'f', 'd'})
# Result: {'b', 'a', 'c', 'f', 'd'}

# intersection(other, ...) или set & other & ... - возвращает пересечение множеств
a = {'a', 'b', 'c', 'd'}
a.intersection({'f','a'})
# Result: {'a'}

# difference(other, ...) или set - other - ... -возвращает множество из всех элементов set, не принадлежащие ни одному из other
a = {'a', 'b', 'c', 'd'}
a.difference({'f','a'})
# Result: {'d', 'b', 'c'}

# symmetric_difference(other); set ^ other - возвращает множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих
a = {'a', 'b', 'c', 'd'}
a.symmetric_difference({'a','d'})
# Result: {'b', 'c'}

# copy() - копия множества
a = {'a', 'b', 'c', 'd'}
d = a.copy()
print(d)
# Result: {'d', 'b', 'a', 'c'}

# update(other, ...); set |= other | ... - объединение множеств. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.update({'w', 'z'})
# print(a)
# Result: {'z', 'b', 'a', 'c', 'w', 'd'}

# intersection_update(other, ...); set &= other & ... - пересечение множеств. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.intersection_update({'a', 'd'})
# print(a)
# Result: {'b', 'c'}

# symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.symmetric_difference_update({'a', 'b'})
# print(a)
# Result: {'c', 'd'}

# add(elem) - добавляет элемент в множество. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.add('w')
# print(a)
# Result: {'w', 'c', 'a', 'd', 'b'}

# remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует. Метод, вносязий изменение в множество
a = {'a', 'b', 'c', 'd'}
a.remove('b')
# print(a)
# Result: {'a','c', 'd'}

# discard(elem) - удаляет элемент, если он находится в множестве. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.discard('b')
# print(a)
# Result: {'a','c', 'd'}

# pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.pop()
# 'c'
# print(a)
# Result: {'a', 'b', 'd'}

# clear() - очистка множества. Метод, вносящий изменения в множество
a = {'a', 'b', 'c', 'd'}
a.clear()
# print(a)
# Result: set()