a=[]
d={}
while a!='':
    a=input().split()
    if a=="":
        break
    if a[0] not in d:
        d[a[0]]=[0,0]
    d[a[0]][0]+=int(a[2])
    d[a[0]][1]+=1
for i in range(11):
    if str(i) not in d :
        print(i,' ','-')
    else:
         print(i,' ',d[str(i)])

