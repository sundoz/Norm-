a=[]
d={}
while a!='':
    a=input().split()
    if a==[]:
        break
    if a[0] not in d:
        d[a[0]]=[0,0]
    d[a[0]][0]+=int(a[2])
    d[a[0]][1]+=1
for i in range(11):
    if str(i+1) not in d :
        print(i+1,' ','-')
    else:
         print(i+1,' ',d[str(i+1)][0]/d[str(i+1)][1])

