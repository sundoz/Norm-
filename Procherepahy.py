n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range (n):
    a=input().split()
    d[a[0]]+=int(a[1])
print(int(d['восток'])-int(d['запад']),' ',int(d['север'])-int(d['юг']))
