text = input()
res = ' '.join(map(lambda word: word.capitalize(), text.split()))
print(res)