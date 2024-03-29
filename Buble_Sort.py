# Список перебирается попарно, сравниваются 2 соседних значения
# Если предыдущее значение больше, то они меняются местами
# И так пока самое большое число не будет в конце списка (всплывет как пузырь)
# И список заново перебирается попарно, выводе пред. топ значение
import random
items = [random.randint(0, 10) for i in range(10)]

def bubble_sort(items):
    # Цикл длиной меньше списка на 1
    for i in range(len(items) - 1):
        # Цикл длиной меньше списка на 1 и уменьшается с увелич. i
        for j in range(len(items) - i - 1):
            # Если следузначение меньше, то меняем их местами
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

print(f'Исходный список: {items}')

result = bubble_sort(items)

print(f'Сортированный список: {result}')
