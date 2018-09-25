import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(arr, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    for el in arr:  # где el - словарь
        slovar = {}
        for arg in args:
            if (arg in el.keys()) and (len(args) == 1):
                yield el[arg]  # генератор выдает только
                #  значения полей
            elif arg in el is not None:
                slovar[arg] = el[arg]  # формируем новый словарь,
                # где пропускаем элементы равные None
        if len(slovar) > 0 and len(args) > 1:
            yield slovar


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    # Необходимо реализовать генератор
    for i in range(num_count):
        yield random.randint(begin, end)
