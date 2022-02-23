poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон-
    используй Python!
'''

f = open('poem.txt', 'w') # открываем для записи(writing)
f.write(poem) # записываем текст в файл
f.close() #закрываем файл

f = open('poem.txt') # Если не указан режим,по умолчанию подразумевается режим чтения('r'eading)

while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла
        break
    print(line, end='')

f.close()