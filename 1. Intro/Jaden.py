def to_jaden_case(text):
    words = text.split()
    jaden_words = [i.capitalize() for i in words]
    return ' '.join(jaden_words)
print(to_jaden_case(input()))