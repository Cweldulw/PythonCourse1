i=0
k=1
n=''
m=0
s1=''
s2=''
a=[]
a1=[0, 0]
#str1="a3b4c2e10b1c3"
str2=''


with open('dataset.txt') as inp:
    str1 = inp.readline().strip()


while i < len(str1):
    s1 = str1[i]
    if i+1 < len(str1):
        s2 = str1[i+1]
    else:
        s2=''
    if not s1.isdigit() and not s2.isdigit():
        a1 = [s1, 1]
        a.append(a1)
    elif not s1.isdigit() and s2.isdigit():
        k=i+1
        while s2.isdigit():
            n = n+s2
            if k+1 < len(str1):
                s2 = str1[k+1]
            else:
                s2=''
            k +=1
        m = int(n)
        n = ''
        a1 = [s1, m]
        a.append(a1)
#    elif s1.isdigit():
    i +=1

str2=''

for i in range(len(a)):
    str2=str2+a[i][0]*a[i][1]

with open('dataout.txt' 'w') as outp:
    outp.write(str2)



#print(str2)