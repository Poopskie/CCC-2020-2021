top = int(input(""))

bot = int(input(""))

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

penis = computeGCD((top % bot), bot)

if top == 0:
    print("0")
elif top%bot == 0:
    print(str(top//bot))
elif top < bot:
    print(str(int((top % bot)/penis)) + '/' + str(int(bot/penis)))
else:
    print(str(top//bot), str(int((top % bot)/penis)) + '/' + str(int(bot/penis)))
