
move = int

square = 1
positions = []


while move != 0:
    move = int(input())

    if move == 0:
        positions.append("You Quit!")
        break


    if square + move < 101:
        square += move
        if square in [9,40,67]:
            if square == 9:
                square = 34
            elif square == 40:
                square = 64
            elif square == 67:
                square = 86
        elif square in [54,90,99]:
            if square == 54:
                square =19
            elif square == 90:
                square  = 48
            elif square == 99:
                square = 77
        elif square  == 100:
            positions.append(100)
            positions.append("You Win!")
            break
    
    positions.append(int(square))

for x in range(len(positions)-1): 
    print("You are now on square", positions[x])

print(positions[-1])










