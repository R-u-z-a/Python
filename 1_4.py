n = int(input("Введите целое положительное число: "))
remainder = n % 10
sum = n
while n >= 0:
    n = n // 10
    if n % 10 > remainder:
        remainder = n % 10
    if n > 10:
        continue
    else:
        print(f"наибольшая цивра в числе {remainder} навна {sum}")
        break
