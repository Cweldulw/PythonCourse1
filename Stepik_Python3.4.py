i=0
k=''
s=''
s1=''
s2=''
n=0
l=''
str1="a3b4c2e10b1"
str2=''




#with open('dataset.txt') as inp:
#    str1 = inp.readline().strip()

while i <= len(str1):
    s = str1[i]
    k = str1[i+1]
    if s.isdigit() and k.isdigit():
        l=s+k
        s2=str1[i-1]
    elif s.isdigit() and not k.isdigit():
        n = int(l)
        str2 = str2 + s2*n
    else:
        k = ''
        s1 = s
        s2 = s
    i +=1


print(str2)