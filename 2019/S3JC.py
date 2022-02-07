horizontals = {} # 0: first 1: second etc
verticals = {}

for i in range(3):
    row = str(input())
    nums = row.split() # returns a list
    int_nums = []
    hi = [0,1,2]
    for x in range(3):
        int_nums.append(nums[x])
    horizontals[i] = {key : nums for key,nums in zip(hi, int_nums)}

for i in range(3):
    verticals[i] = {}
    for x in range(3):
        verticals[i][x] = horizontals[x][i]

# if x at start then x = 3rd - 2nd 
# if x in middle then x = (1st + 3rd)/2
# if x at last then x = 2*(2nd) - 1st 
# lets make a try loop to try finding the x if there is typeerror then move on

#on a better day if you ever come back to this
# also another thing is the numbers are floats rn

def update(hori, vert): # make this shit so that it can put the new found number into the other dict so it ccan be used
    pass


for penis in range(10):
    for x in range(3):
        for i in range(3):
            if horizontals[x][i] == 'X':
                try:
                    if i == 0:
                        horizontals[x][i] = int(int(horizontals[x][2]) - int(horizontals[x][1]))
                    elif i == 1:
                        horizontals[x][i] = int((int(horizontals[x][0]) + int(horizontals[x][2]))/2)
                    elif i == 2:
                        horizontals[x][i] = int(2*int(horizontals[x][1]) - int(horizontals[x][0]))
                except ValueError: 
                    continue

    for i in range(3):
        for x in range(3):
            if horizontals[x][i] == 'X':
                try:
                    if i == 0:
                        horizontals[x][i] = int(int(horizontals[2][x]) - int(horizontals[1][x]))
                    elif i == 1:
                        horizontals[x][i] = int((int(horizontals[0][x]) + int(horizontals[2][x]))/2)
                    elif i == 2:
                        horizontals[x][i] = int(2*int(horizontals[1][x]) - int(horizontals[0][x]))
                except ValueError: 
                    continue
# only using horizontals now


for i in range(3):
    for x in range(3):
        print(horizontals[i][x], end = " ")
    print("\n",end = "")

