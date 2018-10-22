class1 = int(input())
class2 = int(input())
class3 = int(input())

desks1 = ((class1//2)+ (class1 % 2))
desks2 = ((class2//2)+ (class2 % 2))
desks3 = ((class3//2)+ (class3 % 2))

print(desks1+desks2+desks3)
