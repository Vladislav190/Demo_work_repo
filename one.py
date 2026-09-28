def mat(a_11, n):
    matrica = []
    while n != 0:
        matrica.append(a_11)
        a_11 += 1
        n = n - 1
    print(matrica * 2)

per = int(input("Введите первый символ "))
col = int(input("Введите количество "))
mat(per, col)
