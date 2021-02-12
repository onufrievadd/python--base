'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

        m_rows = len(self.my_list)
        self.my_list_size = [(m_rows, len(row)) for row in self.my_list]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.my_list])


    def __add__(self, other):

        if self.my_list_size != other.my_list_size:
            return 'Матрицы разные, сложение невозможно'

        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


matrix1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matrix1, "\n")
matrix2 = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
print(matrix2, '\n')
print(matrix1.__add__(matrix2))