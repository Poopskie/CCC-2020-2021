ah_yes = ""
vowel = "aoiey"
final = []

while ah_yes != "quit!":
    ah_yes = str(input(""))
    if ah_yes == "quit!":
        break

    if len(ah_yes)>4:
        if ah_yes.find("or") == len(ah_yes)-2:
            if ah_yes[ah_yes.find("or")-1] not in vowel:
                hi = ah_yes.replace("or","our")
                final.append(hi)
            else:
                final.append(ah_yes)
        else:
            final.append(ah_yes)
    else:
        final.append(ah_yes)

for x in final:
    print(x)