# Дан список поисковых запросов.
# Получить распределение количества слов в них.
# Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]


element_sum = 0
target_string = ' '
output = []
for element in queries:
    print(element)
    print(element.count(' '))
    output.append(element.count(' ') + 1)
    





print(output)
print(len(output))
print("Из трех слов состоят: ", round(output.count(3)/ len(output) * 100, 2)," %", sep="")
print("Из двух слов состоят: ", round(output.count(2)/ len(output) * 100, 2)," %", sep="")
print("Из одного слова состоят: ", round(output.count(1)/ len(output) * 100, 2)," %", sep="")
