num = int(input())

last_words = []
sorter_lasts = []


for i in range(num*4):
    line = str(input())
    last_words.append(line[line.rfind(" ")+1:].lower())

for i in last_words:
    sorter_lasts.append(i[max(i.rfind("a"),i.rfind("e"),i.rfind("o"),i.rfind("i"),i.rfind("u"),0):])


for i in range(num):
    if sorter_lasts[0+(4*i)] == sorter_lasts[1+(4*i)] == sorter_lasts[2+(4*i)] == sorter_lasts[3+(4*i)]:
        print("perfect")
    elif sorter_lasts[0+(4*i)] == sorter_lasts[1+(4*i)] and sorter_lasts[2+(4*i)] == sorter_lasts[3+(4*i)]:
        print("even")
    elif sorter_lasts[0+(4*i)] == sorter_lasts[2+(4*i)] and sorter_lasts[1+(4*i)] == sorter_lasts[3+(4*i)]:
        print("cross")
    elif sorter_lasts[0+(4*i)] == sorter_lasts[3+(4*i)] and sorter_lasts[1+(4*i)] == sorter_lasts[2+(4*i)]:
        print("shell")
    else:
        print("free")

