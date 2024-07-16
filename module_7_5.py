import os
from time import strftime, localtime

directory = '.'
directory_normalized = os.path.normpath(directory)    # привести к нужному виду в этой ОС

for root, dirs, files in os.walk(directory_normalized):
    for file in files:
        filepath = os.path.join(root, file)    # формирование относительного пути файла
        # filepath = os.path.abspath(file)     # можно использовать такой код для получения абсолютного пути файла
        # filepath = os.path.realpath(file)    # или можно использовать такой код для получения абсолютного пути файла

        filetime = os.path.getmtime(file)    # время последнего изменения контента, выраженное в секундах
        # filetime = os.stat(file).st_mtime    # можно использовать такой код для получения времени послед. изменения
        formatted_time = strftime('%d.%m.%Y %H:%M', localtime(filetime))

        filesize = os.path.getsize(file)
        # filesize = os.stat(file).st_size    # или можно использовать такой код для получения размера файла в байтах

        parent_dir = os.path.dirname(__file__)   # родительская директория файла

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')