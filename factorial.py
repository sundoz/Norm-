def factorial(n):
    a=n
    for i in range(n-1,0,-1):
        a*=i
    return(a)
z=factorial(10)
print(z)