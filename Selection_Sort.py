import random
# создаем список от 1 до 100, длинной 100
items = [random.randint(0, 100) for i in range(100)]

# Функция сортировки списка
def selection_sort(items):

    # Создаем 1 переменную перебора списка
    for num_1 in range(len(items)):
        # min_value - это значение минимального элемента
        # Это может быть как num_1, так и num_2
        min_value = num_1

        # Внутрений цикл для поиска минимального элемента в списке
        # num_2 - переменная идущая впереди num_1
        for num_2 in range(num_1, len(items)):
            # сравнение 2 переменных
            # и если след. элемент от мин. элемента меньше его, то они меняются местами
            if int(items[min_value]) > int(items[num_2]):
                min_value = num_2
        # Элементы меняются местами
        # Если min_value = num_2, то num_1 меняется с num_2
        items[num_1], items[min_value] = items[min_value], items[num_1]
    return items

print(f'Исходный список: {items}')

result = selection_sort(items)

print(f'Сортированный список: {result}')