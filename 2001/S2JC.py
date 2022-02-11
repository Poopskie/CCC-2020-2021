x = int(input(""))
y = int(input(""))

t = y-x+1
x = 1
horizontal = 1 #horizontal nums
vertical = 1 #vertical nums

nums = []

for n in range (x,y+1):
    nums.append(n)

while True:
    if t >= 2*x:
        t -= x*2
        x +=1
        horizontal += 1
        vertical +=1
    elif t >= x:
        t -= x
        vertical +=1
    else:
        break

for x in range (t):
    print(str(nums[len(nums)-(x+1)]),end=" ")




print(nums)

