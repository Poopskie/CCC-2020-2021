# take in input of numbers
# find 2 primes that have the average = the number

from math import sqrt

pee = int(input(""))

primes = [2,3]
results = []

for i in range(4,1000):
    for x in range(2,int(sqrt(i))+1):
        if i % x == 0:
            break
    else:
        primes.append(i)

for i in range(pee):
    num = int(input())

    for i in range(len(primes)):
        if primes[i] <= num*2:
            for x in range(i+1):
                if primes[i] + primes[x] == num*2:
                    results.append(primes[i])
                    results.append(primes[x])
                    break
            else:
                continue
            break
        else:
            break

for i in range(pee):
    print(f"{results[i*2]} {results[(i*2)+1]}")