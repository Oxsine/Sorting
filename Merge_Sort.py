import random
items = [random.randint(0, 10) for i in range(10)]


# функция слияния 2 списков

def split_sort(items):
    # Деление нацело на 2
    N1 = len(items)//2
    # а1 это левая часть списка
    a1 = items[:N1]
    # а2 это правая часть списка
    a2 = items[N1:]
        # Если длина списка больше 1
        # рекурсией вызывается split_sort для a1
    if len(a1) > 1:
        a1 = split_sort(a1)
        # Если длина списка больше 1
        # рекурсией вызывается split_sort для a2
    if len(a2) > 1:
        a2 = split_sort(a2)
        # Передаем 2 списка функции слияния
    return merge_sort(a1, a2)

def merge_sort(items, items_1):
# Создаем 3 пуской список
    new_items = []
# Длины списков
    N = len(items)
    M = len(items_1)
# Переменные для перебора списков
    i = 0
    j = 0
    # Перебор списков
    while i < N and j < M:
        # Если эл. из 1 списка меньше
        # добавляем его в новый список
        if items[i] <= items_1[j]:
            new_items.append(items[i])
            # Переходим дальше по списку
            i += 1
        else:
            new_items.append(items_1[j])
            j += 1
        # Добавляем в новый список последнии элементы
    new_items += items[i:] + items_1[j:]
    return new_items


print(items)

result = split_sort(items)

print(result)


