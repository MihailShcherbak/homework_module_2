def result(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\n'
n = int(input("Привет, введи число от 3 до 20: "))
for k in range(1, 100):
    if n <3 or n >20:
        print(n,'не является числом от 3 до 20, попробуйте ещё раз')
        n = int(input("Введи число ещё раз от 3 до 20: "))
        continue
print(result(n))