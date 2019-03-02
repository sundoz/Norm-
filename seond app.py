with open('input.txt') as r:
    w=  open('output.txt','w')
    с=[]
    d={}
    while True:
        b=r.readline()
        b=b.lower()
        if b!='':
            b=b.split()
            b=[str(i) for i in b]
            for i in range(len(b)):
                if b[i] in d:
                    d[b[i]]+=1
                else:
                    d[b[i]]=1
        else:
            break
    max1=0
    max2=''
    
    for i,j in d.items():
        if max1<j:
            max1=j
            max2=str(i)
            max2+=" "+str(max1)
w.write(max2)
