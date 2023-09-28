money = int(input("Введите сумму вклада под проценты: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

percents = list(per_cent.values())
deposit = []

deposit.append(int((money * (percents[0])) / 100))
deposit.append(int((money * (percents[1])) / 100))
deposit.append(int((money * (percents[2])) / 100))
deposit.append(int((money * (percents[3])) / 100))

print("Максимальная сумма, которую вы можете заработать — ", max(deposit))