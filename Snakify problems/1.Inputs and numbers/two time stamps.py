# b = float(input())
# Print a value:
# print(a, b)
hr1 = int(input())
min1= int(input())
sec1 = int(input())
hr2 = int(input())
min2= int(input())
sec2 = int(input())

time1 = ((hr1*3600)+(min1*60)+(sec1))
time2 = ((hr2*3600)+(min2*60)+(sec2))

print(time2-time1)