# Ввод исходной строки
s = input().strip()

# Ввод границ разворота
i, j = map(int, input().split())

# Разбиваем строку на три части:
# - часть до индекса i
# - подстрока для разворота (от i до j)
# - часть после индекса j
left_part = s[:i]
middle_part = s[i:j]
right_part = s[j:]

# Разворачиваем среднюю часть
reversed_middle = middle_part[::-1]

# Собираем итоговую строку
result = left_part + reversed_middle + right_part

print(result)