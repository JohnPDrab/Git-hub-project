h = int(input())
m = int(input())
s = int(input())

hrs = h+(m/60) + (s/3600)
angle = (hrs/12) * 360
print(angle)