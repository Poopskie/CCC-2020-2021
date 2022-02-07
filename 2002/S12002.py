pink = int(input(""))
green = int(input(""))
red = int(input(""))
orange = int(input(""))
money = int(input(""))

def combinationSum(arr, sum):
    ans = []
    temp = []

    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans
 
def findNumbers(ans, arr, temp, sum, index):
     
    if(sum == 0):
         
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return
       
    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):
 
        # checking that sum does not become negative
        if(sum - arr[i]) >= 0:
 
            # adding element which can contribute to
            # sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
 
            # removing element from list (backtracking)
            temp.remove(arr[i])

 
# Driver Code
arr = [pink,green,red,orange]
sum = money
ans = combinationSum(arr, sum)
 
# If result is empty, then
if len(ans) <= 0:
    print("empty")
     
# print all combinations stored in ans
for i in ans:
    print("# of PINK is", str(i.count(pink)), " # of GREEN is", str(i.count(green)), " # of RED is", str(i.count(red)), " # of ORANGE is", str(i.count(orange)))

print ("Total combinations is " + str(len(ans)) + ".")

ans.sort()

print("Minimum number of tickets to print is", str(len(ans[-1])) + ".")