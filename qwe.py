with open('input.txt')as inf:
    
    out =open ('output.txt','w')
    s=inf.readline()
    s1=''
    s2=''
    a=''
    i=0
    while i<len(s):
        s2=s[i]
        if i==len(s)-1:
                break
        i+=1
      
        while s[i].isdigit() and i<len(s):
            a+=s[i]
            if i==len(s)-1:
                break
            i+=1
          

        
        s1+=s2*int(a)
        a=''

            
    out.write(s1)
