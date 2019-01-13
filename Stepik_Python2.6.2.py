i = int(input())
#a = []
m = 0

for k in range(i):
    for n in range(k+1):
        if m < i:
            print((k+1), end=' ')
            m += 1
#        a.append(k+1)

#for k in range(i):
#    print(a[k], end=' ')