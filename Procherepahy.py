n=int(input())
d={'s':0,'z':0,'u':0,'v':0}
for i in range (n):
    a=input().split()
    d[a[0]]+=int(a[1])
print(int(d['s'])-int(d['u']),' ',int(d['v'])-int(d['z']))
