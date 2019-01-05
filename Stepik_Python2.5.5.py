spisok = [int(i) for i in input().split()]
k = 0

sorted_spisok = sorted(spisok)

while k < len(sorted_spisok):
    element = sorted_spisok[k]
    del sorted_spisok[k]
    if element in sorted_spisok:
        print(element, end =' ')
    while element in sorted_spisok:
        sorted_spisok.remove(element)
        if k > 0:
            k -= 1
    k += 1
