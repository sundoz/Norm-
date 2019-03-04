d={}
d1={}
n=int(input())
for i in range(n):
    d[input().lower()]=''
m=int(input())
for i in range(m):
    a=input().split()
    for j in a:
        if str(j).lower() not in d:
            d1[j]=''
for i in d1.keys():
    print