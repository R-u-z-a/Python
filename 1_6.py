while True:
    deis = 1
    start_km = float(input("Начальный результат: "))
    last_km = float(input("Конечный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результат должен быть больше 0")
    else:
        while start_km < last_km:
            start_km = start_km + 0.1 * last_km
            result_days = start_km
        print(f"Необходимое количество дней {result_days} до результата")
        break

        #У меня ступор не могу понять почему не работает. Потом вроде сделал.
