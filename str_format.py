age = 26
name = 'Pavel'
print('Возраст {0} -- {1} лет.' .format(name, age))
print('Почему {0} забавляется с этим Python' .format(name))
print('Возраст {} -- {} лет.' .format(name, age))
print('Почему {} забавляется с этим Python' .format(name))
# десятичное число (.) с точностью в 3 знака для плавающих :
print('{0:.3}' .format(1/3))
# заполнить подчеркиваниями(_) с центровкой текста (^) по ширине 11:
print('{0:_^11}' .format('Hello'))
# по ключевым словам:
print('{name} написал {book}' .format(name='Swaroop', book='A Byte of Python'))