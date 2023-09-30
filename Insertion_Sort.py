# Сортировка вставками полезна для вставления новых элементов
# в уже отсортированный спискок
# O(n²)
import random
items = [random.randint(0, 10) for i in range(10)]

def insertion_sort(items):
    count = 0
    count_2 = 0
    # Внешний цикл, со 2 до последнего элемента
    for i in range(1, len(items)):
        count += 1
        # Внутренний цикл, декрементация от i
        for j in range(i, 0, -1):
            # если элемент перед j больше, меняем местами
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                count_2 += 1
                # Иначе прерываем внутренний цикл
            else:
                break
    return items


print(f'Исходный список: {items}')

result = insertion_sort(items)

print(f'Сортированный список: {result}')
