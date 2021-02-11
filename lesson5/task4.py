'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus = [['Один', '1'], ['Два', '2'], ['Три', '3'], ['Четыре', '4']]
result = []
fip = open('file_4_new.txt', 'w', encoding='utf-8')
with open('file_4.txt', 'r', encoding='utf-8') as f:
    eng = []
    i = 0
    for line in f:
        fp = line.split()
        eng.append(fp)
    for i, key in enumerate(rus):
        if key[1] == eng[i][2]:
            lp = ' - '.join(key)
            fip.writelines(f'{lp} \n')
            print(lp)
fip.close()

