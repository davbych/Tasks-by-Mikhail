kilom = int(input())
meters = int(input())
kilom *= 1000
if kilom < meters:
    print(kilom)
elif kilom == meters:
    print("Equals")
elif kilom > meters:
    print(meters)