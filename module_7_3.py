class WordsFinder:
    """ Объект этого класса при создании принимает неограниченное количество названий файлов """
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        """
        :return all_words (dict) - {'название файла': [список из слов этого файла]}
        """
        all_words = {}
        for file in self.file_names:    # переберем список с названиями файлов
            with open(file, encoding='utf-8') as an_open_file:    # откроем каждый файл
                text_file = an_open_file.read()      # сохраним считываемое содержимое в переменной
                new_text_file = text_file.lower()    # переведем сохраненное содержимое в нижний регистр
                del_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - '] # список символов, от кот-х нужно избавиться
                for i in range(len(del_punctuation)):
                    new_text_file = new_text_file.replace(del_punctuation[i], "")
                all_words[file] = new_text_file.split()  # добавим данные в словарь по ключу: значения - отдельные слова
        return all_words


    def find(self, word):
        """
        :param word (str) - искомое слово
        :return found_position - {'название файла': <позиция первого найденного слова 'word' в списке слов файла-ключа>}
        """
        word = word.lower()    # перевели искомое слово в нижний регистр
        found_position = {}
        for file, words in self.get_all_words().items():
            position = 0       # при пробеге по новой паре словаря(ключ, значение) - позиция обнуляется
            for i in words:    # перебираем список слов (в словаре в значении) в поиске соответствия искомому слову
                position += 1
                if i == word:
                    found_position[file] = position
                    break     # выход из внутреннего цикла, когда найдено первое совпадение
        return found_position
    
    def count(self, word):
        """
        :param word (str) - искомое слово
        :return number_of_words - {'название файла': <количество найденных слов 'word' в списке слов файла-ключа>}
        """
        word = word.lower()
        number_of_words = {}
        for file, words in self.get_all_words().items():
            count = 0    # новый подсчет в каждой паре ключ-значение
            for i in words:    # перебираем список слов (в словаре в значении) в поиске соответствия искомому слову
                if i == word:
                    count += 1
            number_of_words[file] = count   # добавить итог 'count' после полного прохода по значениям одного ключа
        return number_of_words



# Проверка кода
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())    # вывели все слова в файле в виде списка, без указанной пунктуации
print(finder2.find('TEXT'))       # вывели позицию искомого слова (без учета регистра)
print(finder2.count('teXT'))      # вывели количество искомых слов в файле (без учета регистра)

# # Проверка по файлу 'Mother Goose - Monday’s Child.txt'
# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# # Проверка по файлу 'Rudyard Kipling - If.txt'
# finder1 = WordsFinder('Rudyard Kipling - If.txt')
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# # Проверка по файлу 'Walt Whitman - O Captain! My Captain!.txt'
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# # Проверка кода по нескольким файлам
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
