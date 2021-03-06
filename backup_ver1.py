#Задача
import os
import time
import zipfile

#1. файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"X:\Pictures"','"X:\Radeon ReLive\Instant GIF"']
#Заметьте, что для имен, содержащих пробелы, необходимо использовать
#двойные кавычки внутри строки.

#2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'X:\Backup' #Поставьте ваш путь.

#3. Файлы помещаются в zip-архив.
#4. Имене для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}" .format(target, ' ' .join(source))
#Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')



    
