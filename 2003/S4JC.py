n = int(input())

final = []

for poo in range(n):
    word = str(input())

    combinations = ['']

    for x in range(1, len(word)+1):
        for i in range(len(word)-x+1):
            combinations.append(word[(0+i):(x+i)])

    final.append(len(set(combinations)))

for x in final:
    print(x)





