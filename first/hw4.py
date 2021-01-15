
proceeds = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))


if proceeds > costs:
    print("Результат фирмы - прибыль")
    profit = proceeds - costs
    revenue = (profit / proceeds) * 100
    revenue = round(revenue, 2)
    print(f" Рентабельность выручки {revenue} %:")
    staff = int(input("Введите число сотрудников:"))
    pps = profit / staff
    pps = round(pps, 2)
    print(f"Прибыль фирмы в расчете на одного сотрудника: {pps}")
elif proceeds < costs:
    print("Результат фирмы - убыток")
else:
    print("Фирма работает в ноль")
