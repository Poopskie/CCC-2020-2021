row1 = input()
row2 = input()
row3 = input()

lrow1 = [row1[0],row1[2],row1[4]]
lrow2 = [row2[0],row2[2],row2[4]]
lrow3 = [row3[0],row3[2],row3[4]]

col1 = [row1[0],row2[0],row3[0]]
col2 = [row1[2],row2[2],row3[2]]
col3 = [row1[4],row2[4],row3[4]]

big_row = [lrow1,lrow2,lrow3]
big_col = [col1,col2,col3]

x_location = []

for i in range(len(big_row)):
    x_location.append([])
    try:
        for poo in range(big_row[i].count()):
            x_location[i].append(big_row[i].index("X")+poo)
    except IndexError:
        continue

# x_location should have be a 2d array with the position of the x in each 1d array






