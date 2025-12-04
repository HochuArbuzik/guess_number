def format_name(last, first, middle=None):
    """
    Форматирует имя в формате 'Фамилия И.О.' если есть отчество,
    или 'Фамилия Имя' если отчества нет
    """
    if middle:
        # Берем первую букву имени и отчества
        return f"{last} {first[0]}.{middle[0]}."
    else:
        return f"{last} {first}"


# Основная программа
m = int(input().strip())  # Читаем количество строк

for _ in range(m):
    line = input().strip()
    parts = line.split()
    
    if len(parts) == 2:
        # Формат: Фамилия Имя
        last_name, first_name = parts
        result = format_name(last_name, first_name)
    elif len(parts) == 3:
        # Формат: Фамилия Имя Отчество
        last_name, first_name, middle_name = parts
        result = format_name(last_name, first_name, middle_name)
    else:
        # Если формат неправильный, пропускаем строку
        continue
    
    print(result)