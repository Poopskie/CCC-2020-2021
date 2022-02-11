# take in input of numbers
# find 2 primes that have the average = the number

from math import sqrt

pee = int(input(""))

def is_prime(n):
    end = int(sqrt(n)) +1
    for i in range(2,end):
        if n % i == 0:
            return False
    return True

nums = []

for i in range(pee):
    nums.append(int(input("")))


double = 0
for i in range(pee):
    double = nums[i]*2
    for x in range(2,double):
        if is_prime(x) and is_prime(double-x):
            print(x,double-x)
            break