with open('input.txt') as r:
    mat=0
    fiz=0
    rus=0
    a=0
    w= open('output.txt','w')
    c=0
    while True:
        a=0
        b=r.readline()
        if b!='':
            b=b.split(';')
            b=[str(i) for i in b] 
            mat+=int(b[1])
            fiz+=int(b[2])
            rus+=int(b[3])
            a+=(int(b[1])+int(b[2])+int(b[3]))/3
            w.write(str(a))
            print(file=w)
            c+=1
        else:
            break
    mat=str(mat/c)+' '+str(fiz/c)+' '+str(rus/c)
    w.write(mat)
        
            
            


