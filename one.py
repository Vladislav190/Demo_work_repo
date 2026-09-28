def mat(a_11, n):
    matrica = []
    n1 = n
    while n != 0:
        strok = []
        for i in range(1, n1+1):
            strok.append(a_11)
            a_11 += 1
        matrica.append(strok)
        n = n - 1 
    print(matrica)
per = int(input("Введите первый символ "))
col = int(input("Введите количество "))
mat(per, col)