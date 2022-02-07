m = int(input(""))
a = int(input(""))
b = int(input("")) 

x = b % m # find the number of machines that will have more b than the others

if a > ((m-x)*7): # if you have more than can be splited among the rest of the machines with 1 less b
    final = (b//m + 1) * 7
    poo = (a - ((m-x)*7)) // m # the number of extras after evening out
    final += poo
    if (a - ((m-x)*7)) % m != 0:
        final +=1
else:
    final = (b//m + 1) * 7

print(final)



