
a = int(input("Результат первого дня 'км':"))
b = int(input("Желаемый результат 'км':"))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
a = round(a,2)
print(f"На {day} день спортсмен достигнет результата в {a} км")