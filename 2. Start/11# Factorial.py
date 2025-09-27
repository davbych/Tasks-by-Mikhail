def fact(f):
    for i in range(1, f):
        f*=i
    return f
print(fact(int(input())))