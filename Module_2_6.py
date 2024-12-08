def get_password(number):
    password = []
    for i in range(1, number):
        for j in range(i+1, number):
            if i == j:
                continue
            elif n % (i + j) == 0:
                password.append(i)
                password.append(j)
    return password
n = int(input('Введите целое число от 3 до 20: '))
result = get_password(n)
print('Password:', result)