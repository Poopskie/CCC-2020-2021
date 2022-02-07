#number of input, x,y

n = int(input())

cordsx = []
cordsy = []

for i in range(n):
    cord = str(input())
    cordsx.append(int(cord.split(',')[0]))
    cordsy.append(int(cord.split(',')[1]))
cordsx.sort()
cordsy.sort()

print(f"{cordsx[0]-1},{cordsy[0]-1}")
print(f"{cordsx[-1]+1},{cordsy[-1]+1}")