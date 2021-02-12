'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''
number = int(input("Новый элемент рейтинга: "))
list = [7, 4, 3, 2]
c = list.count(number)
for i in list:
    if c > 0:
        i = list.index(number)
        list.insert(i+c, number)
        break
    else:
        if number > i:
            j = list.index(i)
            list.insert(j, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)