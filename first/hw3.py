n = int(input("Введите число n: "))
m = 0
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n // 10
print(f"Максимальное число: {m}")