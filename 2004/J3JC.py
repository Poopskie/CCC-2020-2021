adj = int(input())
noun = int(input())

adjs = []
nouns = []


for i in range(adj):
    adjs.append(input())

for i in range(noun):
    nouns.append(input())

for i in range(len(adjs)):
    for x in range(len(nouns)):
        print(f"{adjs[i]} as {nouns[x]}")




