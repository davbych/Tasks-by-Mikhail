import random
from random import choice
def quick_sort_deck(deck):
    if len(deck) < 4:
        return sorted(deck)
    elif len(deck) >= 4:
        pivot = random.choice(deck)
        left = []
        right = []
        for l in deck:
            if l <= pivot:
                left.append(l)
        for r in deck:
            if r > pivot:
                right.append(r)
        left.sort()
        right.sort()
        return left+right

print(quick_sort_deck([4,2,7,1,3,5]))
print(quick_sort_deck([10,5,3,8]))
print(quick_sort_deck([1]))
print(quick_sort_deck([3,2]))
print(quick_sort_deck([29, 20, 39, 40, 12, 7, 50, 5, 21, 1, 25, 33, 36, 14, 51, 22, 18, 44, 27, 8, 41, 3, 10, 26, 15, 48, 19, 13, 49, 4, 38, 34, 6, 2, 30, 9, 17, 35, 23, 52, 42, 37, 31, 28, 11, 47, 43, 46, 45, 16, 32, 24]))