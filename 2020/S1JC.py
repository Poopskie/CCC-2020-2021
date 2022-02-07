N = int(input())

time_list = []
distance_list = []
speeds = []

for i in range(N):
    position = str(input())
    positions = position.split()
    time_list.append(positions[0])
    distance_list.append(positions[1])

for x in range(N-1):
    try:
        speed = (int(distance_list[x+1]) - int(distance_list[x]))/int(time_list[x+1])
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







