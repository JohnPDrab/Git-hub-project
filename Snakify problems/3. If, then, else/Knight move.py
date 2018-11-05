x=int(input())
y=int(input())
x1=int(input())
y1=int(input())

distancex = abs(x - x1)
distancey = abs(y - y1)
if distancex == 1 and distancey == 2 or distancex == 2 and distancey == 1:
    print("YES")
else:
    print("NO")    