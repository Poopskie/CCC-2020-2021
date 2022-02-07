# m x n grid cords (Row,Column)
# input specifications: first M (rows), second N (columns)

rows = int(input())
columns = (int(input()))
cords_to_nums = {} # (1,1): 5
nums_to_cords = {} # 5 : [(1,5), (5,1)]

def possible_cords(x): # input number and get possible cords to enter into nums_to_cords
    final_list = []
    list_of_factors = []
    for i in range(1, x+1):
        if x % i == 0: # all possible factors, we want the final cords to be in tuples
            list_of_factors.append(i)
    for i in list_of_factors: # now we have the facotrs we just need to x/i then we can get other pair however we must remmove dups
        final_list.append((i,x//i)) # wat actually we wont ahve dubs
    return(final_list) # list of tuples with cords

for i in range((rows)):
    new_nums_list = []
    numbers = str(input())
    thing = numbers.split() # list of all the numbers in input in str form
    for x in thing:
        new_nums_list.append(int(x))
    for num in range(len(new_nums_list)):
        cord = (i+1, num+1) # the cords as the num increases
        number = new_nums_list[num] # the number on the square
        cords_to_nums[cord] = number
        nums_to_cords[number] = possible_cords(number)

# cant finish this now cuz i gotta go eat
# but basically futuer jackie I already smurfed on this shit for you
# and all you have to do is to but them on square on, and test all the possibilities
# make a for loop for all the possible cords for the number
# then return the new numbers and test the possible cords gtg gl

# do some try, except keyerror

def new_possible_cords(cords, num_to_cord, cord_to_num): #takes in cordinate then returns the next possible cords to add to not_tested
    return num_to_cord[cord_to_num[cords]]


first_possibilities = nums_to_cords[cords_to_nums[(1,1)]] # list of the first possible cords

not_tested = []

for x in first_possibilities:
    not_tested.append(x)


for i in range(1000): # basically since it is infinite and we dont want it to keep going we will do this, we can adjust if TLE
# what I had before was while len(not_tested) < 0:

    

    if not_tested.count(tuple((rows, columns))) != 0:
        print('yes')
        break
    
    if len(not_tested) == 0:
        print('no')
        break

    try:
        for x in nums_to_cords[cords_to_nums[not_tested[0]]]:
            not_tested.append(x)
        not_tested.pop(0)
    except KeyError:
        not_tested.pop(0)

else:
    print('no')






