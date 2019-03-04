
#%%
# 3.1 там уравнение
def f(x):
    
    if x<=-2:
        b=1-(x+2)**2
    elif -2<x<=2:
        b=-x/2
    else:
        b=(x-2)**2+1
        print(b)
        
        
        


#%%
f(5)


#%%
#удаляет из него все нечётные значения, а чётные нацело делит на два
def modify_list(l):
    while i<len(l):
        if l[i]%2!=0:
            del l[i]
        else :
            l[i]=l[i]//2
    return(l)

            


#%%
#Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу. 
#Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].

a=[1,2,3]
d={2:a}
key=2
value=228
d[2]+=[5]
print(d)
def update_dictionare(d,key,value):
    if key in d:
        d[key]+=[value]
    elif key*2 in d:
        d[key*2]+=[value]
    else: 
        d[key*2]=[value]
    return(d)

    
print(update_dictionare(d,key,value))
        
        
    
    
    


#%%
a=[str(i) for i in input().split()]
d={}
for i in a:
    i=i.lower()
    if i in d:
     
        d[i]+=1
    else :
        d[i]=1
for i,j in d.items():
    print(i,' ',j)
        
        


#%%
a


#%%

d={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in d:
        print(d[])
    else:
       
        d[x]=f(x)
        print(d[x])


#%%
with open('input.txt')as inf:
    for line in inf:
        line =line.strip()
        print(line)


#%%
line


#%%



