a=input()
b=input()
c=input()
d=input()
e={}
for i in range(len(a)):
    e[a[i]]=b[i]
for i in range(len(c)):
    print(e[c[i]],end='')
print()
for i in range(len(d)):
    for j in e.keys():
        if d[i]==e[j]:
            print(j,end='')

