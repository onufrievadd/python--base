time = int(input("Введите время в секундах: "))
while time < 0:
    time = int(input("Введите положительное число:"))

hour = time // 3600
minute = (time // 60) % 60
sec = time % 60

print(f"часы: {hour}; минуты: {minute}; секунды: {sec}.")
