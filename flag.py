def flag(N):
    while True:
        try:
            N = int(input('Введите четное число: '))
            if isinstance(N, int):
                if N % 2 == 0:
                    q = 0
                    print('#' * (N * 3 + 2))    # Верхняя граница флага
                    while q in range(0, int(N / 2)):    # Боковые границы и свбодное поле
                        print('#' + ' ' * (N * 3) + '#')
                        q += 1

                    i = ('#' + ' ' * (N + int(N / 2) - 1) + '*')  # Верхняя граница круга и боковыеграницы флага
                    print(i, end='')
                    print(i[::-1])

                    z = 2
                    e = N / 2
                    while z < int(N / 2 + 1):       # Круг
                        k = ('#' + ' ' * (N + int(N / 2) - z) + '*' + 'o' + 'o' * int(N / 2 - e))
                        e -= 1
                        print(k, end='')
                        print(k[::-1])
                        z += 1
                    while z > 2:
                        z -= 1
                        e += 1
                        k = ('#' + ' ' * (N + int(N / 2) - z) + '*' + 'o' + 'o' * int(N / 2 - e))
                        print(k, end='')
                        print(k[::-1])

                    print(i, end='')
                    print(i[::-1])
                    i = 0
                    while i in range(0, int(N / 2)):   # Боковые границы и свбодное поле
                        print('#' + ' ' * (N * 3) + '#')
                        i += 1
                    return '#' * (N * 3 + 2)    # Нижняя граница флага
                else:
                    raise Exception('Введите ЧЁТНОЕ число!\n')
        except Exception as e:
            print('Введите ЧЁТНОЕ число!\n')

print(flag(0))
