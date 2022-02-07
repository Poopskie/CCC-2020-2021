N = int(input())

big_dic = {}
speeds = []
times = []

def sorting(e):
    return int(e)

for i in range(N):
    position = str(input())
    positions = position.split() # positions[0] = time positions[1] = distance
    big_dic[int(positions[0])] = int(positions[1])
    times.append(int(positions[0]))


times.sort(key=sorting)



for x in range(N-1):
    try:
        speed = (big_dic[times[x+1]] - big_dic[times[x]])/(times[x+1] - times[x])
    except ZeroDivisionError:
        continue
    
    if speed >= 0:
        speeds.append(speed)
    elif speed < 0:
        speeds.append(-speed)

largest = 0

for i in speeds:
    if i > largest:
        largest = i

print(largest)







