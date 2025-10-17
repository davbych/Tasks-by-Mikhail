import math
from math import *
def complexy_table(g):
    f = 1
    print("------ n")
    for n in g:
        print(n)
    print("------ O(1)")
    for o1 in g:
        print("1")
    print("------ O(log n)")
    for olog in g:
        print(math.log(olog))
    print("------ O(sqrt(n))")
    for oscrt in g:
        print(sqrt(oscrt))
    print("------ O(n)")
    for on in g:
        print(on)
    print("------ O(n log n)")
    for nolog in g:
        print(nolog*(math.log(nolog)))
    print("------ O(n**2)")
    for n2 in g:
        print(n2**2)
    print("------ O(n**3)")
    for n3 in g:
        print(n3**3)
    print("------ O(2**n)")
    for n22 in g[:3]:
        print(2**n22)
    print("------ O(n!)")
    for of in range(1, g[1]):
        f *= of
        print(f)
    print("------ ")


sizes = [1, 10, 100, 1000, 10000]
print(complexy_table(sizes))