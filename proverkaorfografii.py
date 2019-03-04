n=int(input())
a=[]
d={}
for i in range(n):
    d[input().lower()]=''
m=int(input())

for i in range(m):
    a[i]=input().split()
for i in range(m):
    for j in a[i].lower():
        if j not in d :
            print(j)
            d[j]=''
        
