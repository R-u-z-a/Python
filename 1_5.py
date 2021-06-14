Dokhod = float(input("Введите выручку Вашей компании: "))
Lesion = float(input("Введите издержки вашей компании: "))
Itog = Dokhod - Lesion
if Itog > 0:
    print(f"Доход Вашей компании составляе {Itog}")
    print(f"Издержки Вашей компании составляют {100 * Itog / Dokhod:.1f}%")
    Personal = int(input("Какое количество персонала вы готовы уволить, для повышения доходности? "))
    salary = int(input(f"Введите доход одного сотрудника: "))
    saving = Dokhod * salary + Itog
    print(f"Если вы сократите некоторое количество персонала доход компании повысится {int(Personal) * int(salary) + int(Itog):.2f}")
elif Itog < 0:
    print(f"Ваша компания работает в минус {-Itog}")
else:
    print("Работает в 0")
