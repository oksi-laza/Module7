from os import path    # импортируем 'path', чтобы проверить наличие файла в переменной


class Product:
    """
    :param name (str) - название продукта.
    :param weight (float)- общий вес товара.
    :param category (str) - категория товара.
    """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """ Возвращает единую строку со всеми товарами из файла '__file_name' """
        if not path.exists(self.__file_name):   # если файл в переменной не существует
            create_file = open(self.__file_name, 'w')
            create_file.write('')
            create_file.close()
        open_file_name = open(self.__file_name, 'r')  # сохраним в переменную открытый файл в режиме чтения 'r'
        list_products = open_file_name.read()
        open_file_name.close()
        return list_products

    def add(self, *products):
        for add_product in products:  # перебираем добавляемые продукты
            if add_product.name in self.get_products():  # если добавляемый товар с таким названием уже есть в файле:
                print(f'Продукт {add_product.name} уже есть в магазине')
            else:  # если товара с таким названием нет в файле, то добавляем его в файл со всеми товарами
                open_file_name = open(self.__file_name, 'a')  # откроем файл со всеми товарами в режиме добавления 'a'
                open_file_name.write(f'{add_product}\n')
                open_file_name.close()  # после добавления товара, закроем файл, чтобы сохранились изменения


# Код для проверки
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # строковое представление объекта класса Product

s1.add(p1, p2, p3)

print(s1.get_products())
