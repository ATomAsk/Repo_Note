# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

profit_total = 0
count = 0
my_companies = {}
with open(r".\5-7-in.txt", "r", encoding='utf-8') as my_file:
    for string in my_file:
        item = string.split()
        profit = int(item[2]) - int(item[3])
        if profit > 0:
            my_companies[item[0]] = profit
            profit_total += profit
            count += 1
my_result = [my_companies, {"average_profit": profit_total // count}]

with open("5-7-out.json", "w", encoding='utf-8') as my_json:
    json.dump(my_result, my_json, ensure_ascii=False)
