slova = [i for i in input().lower().split()]

slovar = set(slova)

for slovo in slovar:
    print(slovo, slova.count(slovo))

