# У метода open() существует много аргументов:
#
# 'r' - открытие на чтение(значение по умолчанию)
# 'w' - открытие на запись, содержимое файла удаляется и перезаписывается заново, если файла не существует, создается новый
# 'x' - открытие на запись, только если файла не существует
# 'a' - открытие на дозапись, информация добавляется в конец файла
# 'b' - открытие файла в двоичном виде
# 't' - открытие в текстовом режиме(значение по умолчанию)
# '+' - открытие на чтение и запись
#f = open('C:/Users/admin/PycharmProjects/file.txt', 'r')
f = open('C:/Users/admin/PycharmProjects/file.txt', 'w')
f.write('realistic')