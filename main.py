import os
from pprint import pprint

FILE_PATH = "cook book.txt"
BASE_PATH = os.getcwd()
cook_book = os.path.join(BASE_PATH, FILE_PATH)

def rewrite(file_name):                                              # задание 1
    menu = {}
    with open (cook_book) as book:
        for line in book:
            dish = line.strip()
            a = []
            menu[f'{dish}'] = a
            quantity = int(book.readline())
            for item in range(quantity):
                new_dict = {}
                x = book.readline().split('|')
                new_dict['ingredient_name'] = x[0]
                new_dict['quantity'] = x[1]
                new_dict['measure'] = x[2].strip()
                a.append(new_dict)
            book.readline()
    print('Поваренная книга: \n')
    pprint(menu)

def shopping(dishes, person):                                       # задание 2
    shop_list = {}
    with open (cook_book) as book:
        for line in book:
            line = line.strip()
            if line in dishes:
                iteration = int(book.readline())
                for item in range(iteration):
                    measurement = {}
                    x = book.readline().split('|')
                    measurement['measure'] = int(x[1])*person
                    measurement['quantity'] = x[2].strip()
                    shop_list[f'{x[0]}'] = measurement

    print('\n')
    print('Нужно купить: \n')
    pprint(shop_list)


# rewrite(cook_book)      #
shopping(['Омлет', 'Омлет', 'Фахитос'], 6)
