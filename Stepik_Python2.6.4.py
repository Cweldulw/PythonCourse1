import copy
inp = ''
a = []
b = []

while inp != 'end':
    inp = input()
    if inp != 'end':
        a = [int(i) for i in inp.split()]
        b.append(a)
    else:
        break


c = copy.deepcopy(b)

#print(len(b[0]))
#print(len(b))

for i in range(len(b)):
    for j in range(len(b[0])):
        #c[j][i] = b[j][i-1] + b[j-1][i] + b[j][i-len(b[0])+1] + b[j-len(b)+1][i]
        print(b[i][j - 1] + b[i - 1][j] + b[i][j - len(b[0]) + 1] + b[i - len(b) + 1][j], end = ' ')
    print('')

#for j in range(len(b)):
#    for i in range(len(b[0])):


#print (b)
#print (c)