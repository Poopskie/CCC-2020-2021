r = int(input(""))
c = int(input(""))
grid = []

poo = str(input(""))
for x in poo:
    grid.append(list(poo[x])) #each 2d array contains a vertical line

for i in range(1,r):
    poo = str(input(""))
    for x in range(len(poo)): #character thing in the line
        grid[x].append(poo[x])

m = int(input(""))

for x in range(m):
    move = str(input(""))

'''
for loop for every single position *
nested for loop for the rotations under that position
have another loop to run the simulation
break when the code walks into an X
mark spots that work (make a copy of the original grid)

side cases:
- when you have to rotate at the start (somehow try all rotations at all locations)
- when every single spot works (don't revert changes)
'''


