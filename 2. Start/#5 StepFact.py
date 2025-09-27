def fact(n,k):
    if k<=1:
        return 0
    
    count = 0
    pk=k
    while (n>=pk):
        count+=n//pk
        pk*=k
        
    return count
print(fact(10, 2))