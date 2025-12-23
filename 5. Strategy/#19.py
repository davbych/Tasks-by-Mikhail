def generate_hashtag(s):
    words = s.strip().split()

    if not words:
        return False

    capitalized = ''.join(word.capitalize() for word in words)
    hashtag = '#' + capitalized
    if len(hashtag) > 140:
        return False

    return hashtag

print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
print(generate_hashtag("a" * 140))