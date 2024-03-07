"""
Utilizamos loops para iterar sobre sequências (listas, vetores, matrizes, strings, etc.)

for x in iterable:
    do something


"""
banana = [""] * 6

for i in range("banana".__len__()):
    banana[i] = "banana"[i]

bananaStr = ""

for i in banana:
    bananaStr = bananaStr + i


print(banana)
print(bananaStr)