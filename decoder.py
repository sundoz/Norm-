a2=str(input())
a=[]
b=[]
for i in a2:
    a+=i
b2= input()

for i in b2:
    b+=i
d={}
d1={}
for i in range(len(a)):
    d[a[i]]=b[i]
    d1[b[i]]=a[i]
c=input()
c2=[]
for i in c:
    c2+=i

c1=[]
for i in c2:
    c1+=d[i]
f=input()
f1=[]
f2=[]
for i in f:
    f1+=i
for i in f1:
    f2+=d1[i]
for i in range(len(c1)):
    print(c1[i],end='')
    print()
for j in range(len(f2)):
    print(f2[j],end='')


