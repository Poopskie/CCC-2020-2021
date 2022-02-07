bot = int(input())
top = int(input())

ans = []

for x in range(top):
    if (bot + (x*60)) <= top:
        ans.append((bot + (x*60)))
    else:
        break


for i in range(len(ans)):
    print(f"All positions change in year {ans[i]}")