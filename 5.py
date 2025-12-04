# Читаем количество элементов
n = int(input())

# Если список пустой
if n == 0:
    print(0)
else:
    # Читаем список чисел
    numbers = list(map(int, input().split()))
    
    max_length = 1  # Минимальная длина неубывающего фрагмента
    current_length = 1  # Текущая длина текущего фрагмента
    
    # Проходим по списку, начиная со второго элемента
    for i in range(1, n):
        if numbers[i] >= numbers[i-1]:
            # Если текущий элемент не меньше предыдущего, увеличиваем текущую длину
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            # Если последовательность нарушена, сбрасываем текущую длину
            current_length = 1
    
    print(max_length)