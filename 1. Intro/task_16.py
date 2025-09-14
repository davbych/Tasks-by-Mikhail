from random import shuffle
kolvo = int(input())
s = []
for i in range(kolvo):
    n = list(map(int, input().split()))
    s.append(n)
shuffle(s)
print(*s)
