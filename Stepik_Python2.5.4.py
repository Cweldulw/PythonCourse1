spisok = [int(i) for i in input().split()]


if len(spisok)!= 1:
    for k in range(0, len(spisok)):
        if k==0:
            sum_sosedey = spisok[len(spisok) - 1] + spisok[k + 1]
        elif k==len(spisok)-1:
            sum_sosedey = spisok[k - 1] + spisok[0]
        else:
            sum_sosedey = spisok[k - 1] + spisok[k + 1]
        print(sum_sosedey, end=" ")

else:
   sum_sosedey = spisok[0]
   print(sum_sosedey, end=" ")

