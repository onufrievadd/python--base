'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''




class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            print(data)
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Формат даты не верен'

    @staticmethod
    def valid(data):
        try:
            print(data)
            day, month, year = [int(i) for i in data.split('-')]
        except ValueError:
            return 'Формат даты не верен'
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Такая дата есть'
                else:
                    return f'Год введен не верно'
            else:
                return f'Месяц введен не верно'
        else:
            return f'День введен неверно'

data1 = '12-02-2021'
data2 = '24-12'
data3 = '30-13-2000'
data4 = '21-06-2056'
print(Data.type(data1))
print(Data.type(data2))
print(Data.type(data3))
print(Data.type(data4))
print(Data.valid(data1))
print(Data.valid(data2))
print(Data.valid(data3))
print(Data.valid(data4))