'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('file_3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    my_sum = 0
    print('Зарплата меньше 20.000:')
    for line in f:
        key, value = line.split()
        workers[key] = value
        my_sum += int(value)

        if int(value) < 20000:
            print(key)
print(f'Средний оклад {(my_sum/ len(workers)):.2f}')
