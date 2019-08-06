# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т. е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# добавим расчет максимальной
max_sales = 0
max_sales_channel = ""
for channel in stats:
    #print(stats[channel])
    if  stats[channel] > max_sales:
        max_sales = stats[channel]     
        max_sales_channel = channel
print("Максимальный объем продаж: ", max_sales,"по каналу ", max_sales_channel)
