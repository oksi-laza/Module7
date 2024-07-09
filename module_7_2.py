def custom_write(file_name, strings):
    """
    :param file_name - название файла для записи
    :param strings (list) - список строк для записи
    :return strings_positions (dict) - {(<номер строки>, <байт начала строки>): 'записываемая строка'}
    """
    an_open_file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    number_str = 0
    for string in strings:
        number_str += 1
        strings_positions[(number_str, an_open_file.tell())] = string
        an_open_file.write(f'{string}\n')
    an_open_file.close()
    return strings_positions


# Проверка кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
