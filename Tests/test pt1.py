print("Input -name, -hight, -legnth/radious, -width")

name = input()
h = int(input())
lr = int(input())
w = int(input())

sqpool = (w * lr * h)
cyl = ((3.14*(lr**2))*h)

sqvol = sqpool/7.5
cylvol = cyl/5.875

print(str(name) +" " + str(sqvol) + " " + str(cylvol))
