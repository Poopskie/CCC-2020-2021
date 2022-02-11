n = int(input("")) #initial number of streams

streams = []
pee = 0 # for detecting 99 88 77
woo = 0 #under the 99 (which on is split)
goo = 0 #under the 99 (percentage to the left)
doo = 0 #under the 88 (combining)

for x in range(n):
    poo = int(input(""))
    streams.append(poo)

while pee != 77:
    pee = int(input(""))

    while pee == 99:
        woo = int(input(""))
        goo = int(input(""))
        streams.insert(woo,streams[woo-1]*(100-goo)/100)
        streams[woo-1] = streams[woo-1] * (goo/100)
        break
    
    while pee == 88:
        doo = int(input(""))
        streams[doo-1] = streams[doo-1] + streams[doo]
        streams.pop(doo)
        break

for x in streams:
    print(int(x),end = ' ')