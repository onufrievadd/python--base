'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def my_func(name, surname, ear, city, email, phone):
    print(name, surname, ear, city, email, phone)

name = input("Ваше имя? ")
surname = input("Ваша фамилия? ")
ear = input("Ваш возраст? ")
city = input("Город проживания? ")
email = input("Ваш email? ")
phone = input("Номер телефона? ")

my_func(name, surname, ear, city, email, phone)
