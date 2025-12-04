# Читаем первый список
n = int(input())
list1 = list(map(int, input().split()))

# Читаем второй список
m = int(input())
list2 = list(map(int, input().split()))

# Объединяем списки, сохраняя порядок первого появления
result = []
seen = set()

# Сначала добавляем элементы из первого списка
for num in list1:
    if num not in seen:
        result.append(num)
        seen.add(num)

# Затем добавляем элементы из второго списка
for num in list2:
    if num not in seen:
        result.append(num)
        seen.add(num)

# Выводим результат
print(' '.join(map(str, result)))