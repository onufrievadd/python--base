'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

res_str = '{'
cnt = 0

with open('file_6.txt', 'r', encoding='utf-8') as f:

    for line in f.read().split('\n'):

        subject, lecture, practice, lab = line.split()

        cnt = cnt + 1


        if lecture.find('(') > 0:
            lt = int(lecture[0:lecture.find('(')])
        else:
            lt = 0

        if practice.find('(') > 0:
            pr = int(practice[0:practice.find('(')])
        else:
            pr = 0

        if lab.find('(') > 0:
            lb = int(lab[0:lab.find('(')])
        else:
            lb = 0

        if cnt == 1:
            res_str = res_str + '"' + subject[0:subject.find(':')] + '": ' + str(lt + pr + lb)
        else:
            res_str = res_str + ', ' + '"' + subject[0:subject.find(':')] + '": ' + str(lt + pr + lb)

    res_str = res_str + '}'
    print(res_str)

f.close()





