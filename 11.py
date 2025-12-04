n = int(input())
tokens = input().split()

values = []
for token in tokens:
    if token == 'True':
        values.append(1)
    elif token == 'False':
        values.append(0)
    else:
        try:
            values.append(float(token))
        except ValueError:
            continue

total = sum(values)
average = total / len(values) if values else 0

print(total)
print(f"{average:.6f}")