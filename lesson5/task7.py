'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
profit = {}
sr_profit = {}
my_list = []
prof = 0
prof_over = 0
i = 0
with open('file_7.txt', 'r', encoding='utf-8') as file:
    for line in file.read().split('\n'):
        name, firm, proceeds, costs = line.split()
        profit[name] = int(proceeds) - int(costs)

        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_over = prof / i
        print(f'Прибыль средняя - {prof_over:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    sr_profit = {'средняя прибыль': round(prof_over)}
    my_list.append(profit)
    my_list.append(sr_profit)
    print(f'Прибыль каждой компании - {my_list}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_file = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_file}')