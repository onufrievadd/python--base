'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def need_cloth(self):
        pass

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: { round(coat.need_cloth() + costume.need_cloth()) :.2f}'


class Coat(Clothes):
    @property
    def need_cloth(self):
        return f'Для пошива пальто нужно: { self.param / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):
    @property
    def need_cloth(self):
        return f'Для пошива костюма нужно: { 2 * self.param + 0.3:.2f} ткани'



coat = Coat(44)
costume = Costume(160)
cl = Clothes
print(coat.need_cloth)
print(costume.need_cloth)
print(cl.consumption)
