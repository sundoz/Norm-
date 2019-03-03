n=int(input())
b=[]
d={}
c=''
for i in range(n):
    b=input().split(';')
    if b[0]not in d :
        d[b[0]]=[':',0,' ',0,' ',0,' ',0,' ',0]
    if b[2]not in d :
        d[b[2]]=[':',0,' ',0,' ',0,' ',0,' ',0]
    if int(b[1])>int(b[3]):
        d[b[0]][1]+=1
        d[b[0]][3]+=1
        d[b[2]][7]+=1
        d[b[0]][9]+=3
        
        d[b[2]][1]+=1
    elif int(b[1])<int(b[3]):
        d[b[2]][1]+=1
        d[b[2]][3]+=1 
        d[b[0]][7]+=1
        d[b[2]][9]+=3
        d[b[0]][1]+=1
    else  :
        d[b[2]][1]+=1
        d[b[0]][1]+=1
        d[b[2]][9]+=1
        d[b[0]][9]+=1
        d[b[0]][5]+=1
        d[b[2]][5]+=1

for i,j in d.items():
    print (i,end='')
    for z in j :
        print(z,end='')
    print()



    