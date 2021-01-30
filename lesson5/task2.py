'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

f = open('file_2.txt')
line = 0
for i in f:
    line += 1

    space = 0
    word = 0
    for j in i:
        if j != ' ' and space == 0:
            word += 1
            space = 1
        elif j == ' ':
            space = 0

    print(f'{i}\n {word} слов\n')

print(f'Всего {line} строк')
f.close()