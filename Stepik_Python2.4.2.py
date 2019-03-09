S = input()
i = 0
k = 0
a = ''
c = ''
while i <= len(S) - 1:
    if i != 0:
        a = S[i - 1]
    b = S[i]
    i += 1
    if b != a:
        if k != 0:
            c = c + str(k) + b
            k = 1
        else:
            c = b
            k += 1
    else:
        k += 1
print(c + str(k))
