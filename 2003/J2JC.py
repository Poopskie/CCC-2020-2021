import math

hi = int

f1s = []
f2s = []

while hi != 0:
    hi = int(input())

    if hi == 0:
        break

    factors = []

    for x in range(1,hi+1):
        if hi % x == 0:
            factors.append(x)


    if len(factors)%2 ==0:
        f1s.append(int(factors[int(len(factors)/2)-1]))
        f2s.append(int(factors[int((len(factors)/2))]))
    elif len(factors) % 2 == 1:
        f1s.append(int(math.sqrt(hi)))
        f2s.append(int(f1s[-1]))

for i in range(len(f1s)):
    print("Minimum perimeter is", str((f1s[i]*2)+(f2s[i]*2)),"with dimensions", str(f1s[i]),"x",str(f2s[i]))


