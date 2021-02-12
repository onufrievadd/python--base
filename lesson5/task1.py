'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

f = open('file_1.txt', 'w',encoding='utf-8')
print('Введите строки: ')
while True:
    s = input()
    if s == '':
        break
    f.write(s + '\n')
f = open('file_1.txt', 'r')
for line in f:
    print(line)
f.close()