def to_jaden_case(text):
    words = text.split()
    jaden_words = [word.capitalize() for word in words]
    return ' '.join(jaden_words)
print(to_jaden_case(input()))