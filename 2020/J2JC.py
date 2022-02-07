# threashold, number people with disease, how many they infect

needed = int(input())
start = int(input())
daily = int(input())

day = 0
total = start

if daily == 1:
    total = needed+1
    day = int(needed/(start))


while total <= needed:
    day+=1
    total = (start*(daily**(day+1) - 1))/(daily-1)



print(day)

