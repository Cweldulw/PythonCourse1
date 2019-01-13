b=0
s=0

inp = int(input())
a = [[0 for j in range(inp)] for i in range(inp)]

# i - ширина, j - длина

while inp-s >= 2:
    for i in range(inp-s):
        b = b + 1
        a[s//2][i+s//2] = b

    for j in range(inp-1-s):
        b = b + 1
        a[j+1+s//2][inp-1-s//2] = b

    for i in range(inp-1-s):
        b = b + 1
        a[inp-1-s//2][-i-2-s//2] = b

    for j in range (inp-2-s):
        b = b + 1
        a[-j-2-s//2][s//2] = b

    s = s+2

if inp-s == 1:
    b= b + 1
    a[inp//2][inp//2]=b

for j in range(inp):
    for i in a[j]: print(i, end=" ")
    print()

