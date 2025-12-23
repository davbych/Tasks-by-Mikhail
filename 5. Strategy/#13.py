def hamming(n):
    if n <= 0:
        raise ValueError("n должно быть положительным целым числом")

    ham = [1]
    i2 = i3 = i5 = 0
    while len(ham) < n:
        next2 = ham[i2] * 2
        next3 = ham[i3] * 3
        next5 = ham[i5] * 5
        next_ham = min(next2, next3, next5)
        ham.append(next_ham)

        if next_ham == next2:
            i2 += 1
        if next_ham == next3:
            i3 += 1
        if next_ham == next5:
            i5 += 1

    return ham[n - 1]


print([hamming(i) for i in range(1, 21)])
print(hamming(20))
print(hamming(5000))
