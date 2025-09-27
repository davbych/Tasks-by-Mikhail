def f(k1):
    k2=k1+1
    n=1
    while True:
        p1=n*k1
        p2=n*k2
        if sorted(str(p1))==sorted(str(p2)):
            print(n)
            break
        n+=1
print(f(325))