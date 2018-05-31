def Eur(n):
    ls = []
    result = 0
    for i in range(1, n):
        ls.append(i*(i+1)/2)
    for a in range(1, n):
        for b in range(a, n):
                if n - a*(a+1)/2 - b*(b+1)/2 in ls:
                    result = 1
                    return print(result)
                else:
                    pass
    return print(result)

k = input()
for _ in range(int(k)):
    n = int(input())
    Eur(n)
