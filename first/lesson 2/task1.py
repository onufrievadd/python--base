'''
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
пользователя, а указать явно, в программе.
'''

infloat = 2.3
inint = 10
incomplex = 5+6j
instr = "Hello world"
inlist = ['a', '1']
intuple = ('b', '2')
indict = {'country': 'Russia', 'city': 'Moscow'}

list = [infloat, inint, incomplex, instr, inlist, intuple, indict]
for i in list:
    print(f'{i} is {type(i)}')