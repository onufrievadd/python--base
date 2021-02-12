'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        dividend = int(input('Введите делимое: '))
        divider = int(input('Введите делитель: '))
        if divider == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            result = dividend / divider
            return result
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(f'Результат деления:{div():.2f}')
