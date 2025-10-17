from itertools import permutations

def is_anagram_method1(s1, s2):
    count = 0
    lenght = len(s1)
    for i in s1:
        for j in s2:
            if i==j:
                count+=1
    if lenght == count:
        return True
    else:
        return False

def is_anagram_method2(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def is_anagram_method3(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in permutations(s1):
        if ''.join(i) == s2:
            return True
    return False

def is_anagram_method4(s1, s2):
    if len(s1) != len(s2):
        return False
    char_count1 = {}
    char_count2 = {}
    for char in s1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in s2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2


print(is_anagram_method1("python", "tyhpon"))
print(is_anagram_method2("python", "tyhpon"))
print(is_anagram_method3("python", "tyhpon"))
print(is_anagram_method4("python", "tyhpon"))