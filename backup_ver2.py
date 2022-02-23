import os
import time
import zipfile
source = ['"C:\\Users\Godless\Pictures"', 'C:\\Users\Godless\Documents\Diablo II']
target_dir = ['X:\Games']
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}" .format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')
    
