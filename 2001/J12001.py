num = int(input("enter"))
for x in range(num*2+1):
    if x % 2 == 1:
        print('*'*(num-abs(num-x)) + ' '*abs((num*2)-(x*2)) + '*'*(num-abs(num-x)))