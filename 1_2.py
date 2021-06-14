tea = int(input("Введите время в секундах: "))
sec = tea
min = sec // 60
hour = tea // 3600

sec2 = sec % 60
min2 = min % 60
print(f"{hour:02}:{min2:02}:{sec2:02}")
