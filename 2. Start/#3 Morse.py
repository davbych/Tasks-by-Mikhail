morse = {
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----',
' ': '/'}

k = []
text = input("Word(-s): ")
for i in text.upper():
    if i in morse:
        k.append(morse[i])
result="".join(k)
print(f"{text} - {result}")

km = []
textm = input("Morse: ")
reverse = {v: k for k, v in morse.items()}

for word in textm.split("/"):
    for im in word.split():
        if im in reverse:
            km.append(reverse[im])
resultm=''.join(km)
print(f"{textm} - {resultm}")