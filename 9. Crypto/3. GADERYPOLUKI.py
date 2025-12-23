def gaderypoluki(text: str, key: str, mode: str = "encode") -> str:
    key = key.lower()

    slovar = {}
    for i in range(0, len(key), 2):
        k1, k2 = key[i], key[i+1]
        slovar[k1] = k2 #k1: k2
        slovar[k2] = k1 #k2: k1
        slovar[k1.upper()] = k2.upper() #K1: K2
        slovar[k2.upper()] = k1.upper() #K2: K1

    result = ''.join(slovar.get(i, i) for i in text) #a: g => g; A: G => G
    return result

print(gaderypoluki("ABCD", "agedyropulik", "encode"))
print(gaderypoluki("Ala has a cat", "gaderypoluki", "encode"))
print(gaderypoluki("Dkucr pu yhr ykbir","politykarenu", "decode"))
print(gaderypoluki("Hmdr nge brres","regulaminowy", "decode"))