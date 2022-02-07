m = int(input(""))
n = int(input(""))
count = 0
new_x = ''

for x in range(m,n+1):
    for f in str(x):
        if f == str(9):
            new_x = str(6) + new_x
        elif f == str(6):
            new_x = str(9) +  new_x 
        elif f == str(1) or f== str(8) or f == str(0):
            new_x = f + new_x 
        else:
            new_x = '0'
    if int(new_x) == x:
        count += 1
    new_x = ''
    

print(count)