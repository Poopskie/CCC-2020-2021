# Given some text, T T , and a string, S S , determine if T T contains a cyclic shift of S S .

text = str(input())
shifted = str(input())

possible_shifted = []

for i in range(len(shifted)):
    possible_shifted.append(shifted[i:] + shifted[0:i])

result = "no"


for words in possible_shifted:
    if text.find(words) != -1:
        result = "yes"


print(result)






