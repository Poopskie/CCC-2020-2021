quarter = int(input(""))
mac1 = int(input(""))
mac2 = int(input(""))
mac3 = int(input(""))

plays = 0

while quarter > 0:
    if quarter >= 3:
        mac1 += 1
        mac2 += 1
        mac3 += 1
        quarter -= 3
        plays +=3
    elif quarter >= 2:
        mac1 += 1
        mac2 +=1
        quarter -=2
        plays +=2
    elif quarter >= 1:
        mac1 +=1
        quarter -=1
        plays +=1
    
    if mac1 == 35:
        quarter += 30
        mac1 = 0
    if mac2 == 100:
        quarter += 60
        mac2 = 0
    if mac3 == 10:
        quarter +=9
        mac3 = 0



plays += quarter

print("Martha plays", str(plays),  "times before going broke.")
