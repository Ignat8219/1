money = int(input("введите сумму"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
percent = list(per_cent.values())
deposit = [num*money/100 for num in percent]
deposit_max = max(deposit)
print(deposit)
print("Максимальная сумма, коорую вы можете заработать - ", deposit_max)





