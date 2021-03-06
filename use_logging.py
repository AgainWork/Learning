import os
import platform
import logging

if platform.platform().statrswith('windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
        os.getenv('HOMEPATH'), \
            'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("Сохраняем лог в", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debag("Начало программы")
logging.info("какие-то действия")
logging.warning("Программа умирает")

