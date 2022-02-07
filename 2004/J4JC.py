key = str(input())
message = str(input())


new_message = ""
keys = []

alph = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(message)):
    if alph.find(message[i].lower()) == -1:
        continue
    else:
        new_message += message[i]

for i in range(len(key)):
    keys.append(alph.find(key[i].lower()))

ans = ""

for i in range(len(new_message)):
    ans += alph[(alph.find(new_message[i].lower())+keys[i%(len(keys))])%26]

print(ans.upper())

