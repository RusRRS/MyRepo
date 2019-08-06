# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т. е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# Вариант 2. Решение на списках.
unique_ids_2 = [] # пустой список для уникальных значений

for value_list in ids:
    ids_list = ids[value_list]
    for element in ids_list:
        if element not in unique_ids_2:
            unique_ids_2.append(element)
print(unique_ids_2)
