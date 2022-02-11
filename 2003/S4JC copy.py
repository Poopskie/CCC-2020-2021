n = int(input())

final = []

for i in range(n):
    word = str(input())

    combinations = [word[(0+i):(x+i)] for x in range(1, len(word)+1) for i in range(len(word)-x+1)]
    combinations.append('')

    final.append(len(set(combinations)))

for x in final:
    print(x)





