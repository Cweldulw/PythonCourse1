lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if x not in lst:
            break
        else:
            print(lst.index(x), end = ' ')
            lst[lst.index(x)] = 'a'